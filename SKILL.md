---
name: go-diggy-animation-production
description: Turn a Go! Diggy brief and confirmed character assets into a traceable storyboard, Doubao handoff, archived-media audit, real-audio subtitle package, and evidence-backed delivery. Use for new episodes, promos, covers, production write-ups, or reusable handoffs; enforce two intentional camera positions per shot, action-triggered changes, explicit role/vehicle identity, pauses, and evidence-backed delivery; do not use it to override the project's current master specification.
metadata:
  short-description: Build traceable Go! Diggy episode packages
---

# Go! Diggy Animation Production

Use this skill when the task concerns the Go! Diggy construction-vehicle animation series and the user needs more than an idea: a storyboard, shot prompts, an asset handoff, a production experience write-up, a promo package, or a verified delivery package.

Author: Leo Builds (@leomadeits), who also created `cartoon-from-design` and the Rory & Pip production article. This skill carries the author's own lessons—treat the visual source as a specification, make changes reproducible, and require visual evidence—into Go! Diggy's production chain: confirmed character/vehicle references, storyboard images, Doubao-generated clips, real audio, subtitles, and 720p QA.

## Authority and discovery

When working inside the Go! Diggy project, read these files before production work:

1. `Go_Diggy_动画制作总规范.md`
2. `Go_Diggy_动画规范_横屏.md` or `Go_Diggy_动画规范_竖屏.md`
3. `Go_Diggy_固定工作流.md`
4. `00_项目资料/角色_封面_分镜/01_角色设定/前30集固定人物参考/README.md`
5. `00_项目资料/角色_封面_分镜/01_角色设定/角色命名与素材索引.md`
6. The relevant episode execution note, when one exists.

The current project documents are the authority. This skill, the author's related production article, old skills, old scripts, filenames, and modification times must not override them. In a portable checkout where those files are absent, ask for or create an equivalent project contract and asset register instead of inventing one.

## Non-negotiable rules

- **Reference assets are specifications.** Use confirmed character/vehicle assets as the fixed basis. Change only the scene, action, expression, staging, and camera required by the shot. Do not redesign faces, proportions, colors, materials, mechanical structures, or fixed recognition points. Reject distorted generations.
- **The storyboard is intent, not audio evidence.** Prompts and boards describe the desired action and dialogue intent. Subtitles and dialogue claims come from the archived video's actual audio and ASR/listening review.
- **No external result is an asset until it is archived.** A clip generated in Doubao but not downloaded into the episode's source folder is not an integrated shot and must not be called a candidate delivery.
- **Separate states.** Keep `draft`, `candidate`, `archived`, `qa_passed`, and `user_confirmed` distinct. A newer filename, larger version number, or word such as “final” is not confirmation evidence.
- **Prove repairs.** After a change, produce the evidence that can reveal the defect: reference-versus-output comparisons, close-ups of joins, representative frame sheets, audio/subtitle checks, and a playable export. Never report “fixed” from code or intention alone.
- **Preserve replayability.** Keep the manifest, source paths, prompt version, edit timeline, ASR/subtitle source, QA evidence, and change notes together. Do not overwrite an older candidate before the new one is verified.
- **Respect the current output contract.** The current series contract is 720p: 1280×720 for horizontal and 720×1280 for vertical video. Follow the selected appendix for subtitle coordinates, Logo behavior, and delivery variants. Do not silently revive historical 1080p settings.
- **Keep the character base clean and child-safe.** Do not add heavy mud, grime, logos, or body alterations unless the story and current project rules explicitly require them. Rolly's normal wide drum must remain normal and wide.
- **Every shot prompt uses two real camera positions.** A roughly ten-second shot must fuse at most two genuinely different positions in the same copyable paragraph; the second position cannot be a digital zoom, crop, or coaxial slide. Change position when an action changes—such as braking, a hand gesture, bucket movement, bridge movement, material entering water, or a vehicle entering—rather than using a fixed mid-shot cut. Prefer spatially readable changes such as wide-to-medium reaction or action-medium-to-mechanical insert; use only motivated tracking, lateral movement, gentle push/pull, low-angle lift, waterline diagonal slide, or action-triggered cuts. Keep the established axis; do not use random shake, spinning, fast zooms, meaningless orbits, pure rear/side-rear views, or angles that hide character identity.

- **Name each on-screen character or vehicle by type.** In every shot paragraph, the first mention of each actual on-screen subject must include its name, human/vehicle type, one or two fixed recognition points, and its current action. Never give the generator only a name such as Ben or Diggy. Use the confirmed project index: Ben/小本 is the builder human, Diggy/迪奇 is the yellow excavator, Rolly/罗利 is the teal-green road roller with a normally wide drum, Dumpy/丹比 is the red-and-yellow small dump truck, and Carry/凯瑞 is the flatbed truck. Describe only subjects actually appearing in that shot; type descriptions must not add extra characters or vehicles.

- **Keep speech and reaction timing child-readable.** Use roughly 110–125 WPM for explanation, 125–140 WPM for short action peaks, leave about 0.4–0.7 seconds after a key action and 0.7–1.0 seconds for a fault/reaction beat, and derive final subtitles only from the actual archived audio and ASR/listening review.
- **Do not publish secrets.** Never put tokens, API keys, private attachments, or local absolute paths into the Skill, README, manifest examples, Git history, or public issue. Public publishing requires a specific destination repository; creating or pushing to one is a separate authorized action.

## Production loop

### 1. Classify the requested artifact

Decide whether the user wants an episode, a short promo, a cover, a production write-up, or a release/handoff package. For a write-up or Skill, extract the reusable decision rules and evidence gates; do not claim that a video was produced merely because a storyboard or prompt exists.

### 2. Lock the contract and inventory

Record the current master specification, selected aspect appendix, workflow, episode note, confirmed character assets, Logo paths, and intended language versions in a manifest. Use `references/episode-manifest.example.json` as the minimum shape. Mark anything not yet located as `unlocated`, not as complete.

### 3. Define the story and storyboard

Build about ten storyboard beats for a normal episode. Treat ten seconds as a planning rhythm, not a forced final duration. Each shot should state:

- shot ID and continuity anchor;
- who/vehicle appears and the fixed asset used;
- location, prop state, object state, and spatial axis;
- one primary action and the intended reaction or pause;
- dialogue intent, without pretending it is the final spoken line;
- camera and composition;
- negative constraints: no text, subtitles, Logo, watermark, extra vehicles, or character deformation.

One independent, copyable prompt belongs to one shot. The paragraph must include each actual on-screen subject's name, human/vehicle type, fixed recognition point, and current action on first mention; it must also fuse the spatial axis, two motivated camera positions, camera movement, dialogue intent, speech speed, pauses, and negative constraints. Preserve prop and object state across adjacent shots.

### 4. Handoff to generation

Generate or select storyboard images using the confirmed references. Only after the storyboard image is accepted, prepare the Doubao prompt package. The user downloads and archives generated clips in the episode's `01_原始镜头/` folder; retain clear shot/version names and do not overwrite previous candidates.

### 5. Audit the real media

For every archived candidate, verify that it decodes and record duration, dimensions, frame rate, audio presence, audio duration, visual continuity, and deformation points. Sample real frames and listen to the actual audio. A board, prompt, screenshot, or filename cannot substitute for this check.

### 6. Edit from the real timeline

Use one timeline as the source of truth for source clip, trim in/out, speed, audio offset, and final time range. Recalculate downstream timing after any edit. Derive dialogue subtitles from the actual final audio; derive top keywords only from actual speech or a clearly synchronized action. Chinese versions use English above Chinese; English versions use English only.

### 7. QA and state the result precisely

Run the relevant checks in `references/qa-checklist.md`. Inspect representative opening, character-introduction, title-card, action, replacement, ending, and close-up frames; play the complete file; check subtitles, Logo, audio, dimensions, and file paths. Report each item as `verified`, `not verified`, `blocked`, or `not applicable`, with evidence.

### 8. Package the handoff

Deliver only what exists: manifest, storyboard/prompt package, archived source references, playable exports, subtitle files, QA evidence, and a change log. This distribution includes the author's existing Chinese/English v05 promos in `demo/`, and 16 project images in `assets/gallery/`; consult `references/media-index.json` for provenance. These are portfolio examples, not automatically approved production references for a new episode. For an illustrated write-up, select relevant real project examples and explain what each shows. Keep character reference, storyboard, cover and rendered footage labels accurate. Follow `references/promo-video.md` when replacing a promo.

## Reusable references

- Read [production-experience.md](references/production-experience.md) when writing or explaining the Go! Diggy method.
- Read [qa-checklist.md](references/qa-checklist.md) before reporting a candidate, QA pass, or delivery.
- Read [episode-manifest.example.json](references/episode-manifest.example.json) when starting a new package or auditing state.
- Read [promo-video.md](references/promo-video.md) when adding a trailer or README video introduction.

The validator at `scripts/validate_manifest.py` checks the portable manifest shape and state gates. It does not prove that a video, audio track, visual asset, or user confirmation exists; those still require media and human-facing evidence.
