#!/usr/bin/env python3
"""Validate the portable Go! Diggy episode manifest shape and state gates."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


STATES = {
    "draft",
    "candidate",
    "archived",
    "qa_passed",
    "user_confirmed",
    "unlocated",
    "not_applicable",
}
AUDIO_STATES = {"not_started", "unverified", "verified", "blocked", "not_applicable"}
QA_STATES = {"not_started", "in_progress", "pass", "fail", "blocked"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()

    errors: list[str] = []
    try:
        data = json.loads(args.manifest.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"FAIL: manifest not found: {args.manifest}")
        return 1
    except json.JSONDecodeError as exc:
        print(f"FAIL: invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}")
        return 1

    if not isinstance(data, dict):
        print("FAIL: top-level manifest must be an object")
        return 1

    for key in ("schema_version", "project", "episode", "source_contract", "canvas", "characters", "shots", "audio", "subtitles", "outputs", "qa"):
        if key not in data:
            errors.append(f"missing top-level key: {key}")

    source = data.get("source_contract", {})
    if isinstance(source, dict):
        for key in ("master_spec", "aspect_spec", "workflow", "status"):
            if not source.get(key):
                errors.append(f"source_contract.{key} must be recorded")
        if source.get("status") not in STATES:
            errors.append("source_contract.status is not a known state")
    else:
        errors.append("source_contract must be an object")

    canvas = data.get("canvas", {})
    if isinstance(canvas, dict):
        width = canvas.get("width")
        height = canvas.get("height")
        aspect = canvas.get("aspect")
        if not isinstance(width, int) or not isinstance(height, int):
            errors.append("canvas.width and canvas.height must be integers")
        elif aspect == "16:9" and (width, height) != (1280, 720):
            errors.append("16:9 video canvas must be 1280x720")
        elif aspect == "9:16" and (width, height) != (720, 1280):
            errors.append("9:16 video canvas must be 720x1280")
        if not isinstance(canvas.get("language_versions"), list) or not canvas["language_versions"]:
            errors.append("canvas.language_versions must be a non-empty list")
    else:
        errors.append("canvas must be an object")

    characters = data.get("characters", [])
    if not isinstance(characters, list) or not characters:
        errors.append("characters must be a non-empty list")
    else:
        for index, character in enumerate(characters, start=1):
            if not isinstance(character, dict):
                errors.append(f"characters[{index}] must be an object")
                continue
            for key in ("name_en", "name_zh", "asset_path", "state"):
                if not character.get(key):
                    errors.append(f"characters[{index}].{key} must be recorded")
            if character.get("state") not in STATES:
                errors.append(f"characters[{index}].state is not a known state")

    shots = data.get("shots", [])
    if not isinstance(shots, list) or not shots:
        errors.append("shots must be a non-empty list")
    else:
        shot_ids: set[str] = set()
        for index, shot in enumerate(shots, start=1):
            if not isinstance(shot, dict):
                errors.append(f"shots[{index}] must be an object")
                continue
            shot_id = shot.get("id")
            if not shot_id:
                errors.append(f"shots[{index}].id must be recorded")
            elif shot_id in shot_ids:
                errors.append(f"duplicate shot id: {shot_id}")
            else:
                shot_ids.add(shot_id)
            for key in ("source_image", "prompt_path", "video_path", "video_state", "audio_state"):
                if not shot.get(key):
                    errors.append(f"shots[{index}].{key} must be recorded")
            if shot.get("video_state") not in STATES:
                errors.append(f"shots[{index}].video_state is not a known state")
            if shot.get("audio_state") not in AUDIO_STATES:
                errors.append(f"shots[{index}].audio_state is not a known state")

    for section_name in ("audio", "subtitles"):
        section = data.get(section_name, {})
        if not isinstance(section, dict):
            errors.append(f"{section_name} must be an object")
        elif section.get("status") not in AUDIO_STATES:
            errors.append(f"{section_name}.status is not a known state")

    outputs = data.get("outputs", [])
    if not isinstance(outputs, list) or not outputs:
        errors.append("outputs must be a non-empty list")
    else:
        for index, output in enumerate(outputs, start=1):
            if not isinstance(output, dict):
                errors.append(f"outputs[{index}] must be an object")
                continue
            for key in ("path", "variant", "state"):
                if not output.get(key):
                    errors.append(f"outputs[{index}].{key} must be recorded")
            if output.get("state") not in STATES:
                errors.append(f"outputs[{index}].state is not a known state")

    qa = data.get("qa", {})
    if not isinstance(qa, dict):
        errors.append("qa must be an object")
    else:
        qa_status = qa.get("status")
        if qa_status not in QA_STATES:
            errors.append("qa.status is not a known state")
        evidence = qa.get("evidence")
        if not isinstance(evidence, list):
            errors.append("qa.evidence must be a list")
        if qa_status == "pass" and not evidence:
            errors.append("qa.status=pass requires at least one evidence item")
        if isinstance(outputs, list):
            for index, output in enumerate(outputs, start=1):
                if isinstance(output, dict) and output.get("state") == "user_confirmed":
                    if qa_status != "pass":
                        errors.append(f"outputs[{index}] cannot be user_confirmed before qa.status=pass")
                    if output.get("sha256") in (None, "", "unrecorded"):
                        errors.append(f"outputs[{index}] user_confirmed requires a recorded sha256")

    if errors:
        print(f"FAIL: {len(errors)} issue(s) in {args.manifest}")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"PASS: manifest structure and state gates are valid: {args.manifest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
