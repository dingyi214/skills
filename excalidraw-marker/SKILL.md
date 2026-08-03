---
name: excalidraw-marker
description: Apply the **marker** look to Excalidraw diagrams — Excalidraw native color **pairs** (saturated stroke + light same-hue fill), extra-bold solid rounded strokes, pure black/white text & lines, hand-drawn font. Use when drawing a new `.excalidraw`, or restyling an existing diagram to the house style; triggers on "marker 风", "excalidraw 风格 / 上色", "重画 / 重写 .excalidraw".
---

# 卡通 Marker 风

A shape's stroke and fill are always a **pair** — same hue, a saturated stroke plus its light fill, drawn from Excalidraw's native palette. Text and lines are pure black on light, pure white on dark. The whole feel is **marker**: thick, bold, hand-drawn.

## Two branches

### Drawing a new diagram

Build every shape with the marker parameters:

- **Pair** — `strokeColor` = a native saturated hue, `backgroundColor` = its light fill (table below). Same hue, always.
- `strokeWidth: 4` (extra-bold) · `strokeStyle: solid` · `roughness: 0` · `roundness: {type: 3}`
- `fillStyle: solid`
- Text — pure `#000000` (on a light fill) or `#FFFFFF` (on a dark board). `fontFamily: 1` (Virgil, hand-drawn) for English and Chinese alike.
- Lines / arrows — pure `#000000` / `#FFFFFF`, `strokeWidth: 4`, `roundness: {type: 2}` on arrows.
- Labels go on the shape's bound `text` field (it auto-centres), not a separate text element — except titles over large background boards, which stay free-standing (a bound label would centre on the board and cover its content).

### Restyling an existing diagram

Run `transform.py` against the file. It snaps every shape's colours to the nearest native **pair** and forces the marker stroke / text rules, preserving layout:

```bash
python3 transform.py path/to/diagram.excalidraw
```

**Completion criterion** — every rectangle / ellipse / diamond carries a native pair (stroke = a saturated hue from the table, fill = its light fill), every text element is `#000000` or `#FFFFFF`, every stroke is `strokeWidth 4 · solid`. Check the file by listing distinct `backgroundColor` / `strokeColor` values; any value not in the table means a shape was missed.

## The native pairs

Excalidraw's own palette — stroke (saturated) + fill (light, same hue):

| stroke | fill | feel |
|---|---|---|
| `#e03131` red | `#ffc9c9` | error / critical |
| `#e8590c` orange | `#ffd8a8` | async / event |
| `#2f9e44` green | `#b2f2bb` | success / healthy |
| `#0c8599` cyan | `#99e9f2` | data / store |
| `#1971c2` blue | `#a5d8ff` | primary / link |
| `#9c36b5` purple | `#eebefa` | service / middleware |
| `#868e96` gray | `#e9ecef` | note / secondary / board |
| `#1e1e1e` black | `#ffffff` | default text / border |

Source: Excalidraw's built-in design guide. Limit one diagram to 3–4 hues — a rainbow reads as noise.

## Dark boards

On a deep background (`#0F172A` and the like) flip the ink: white text, white lines, white strokes; cards on the board still take a light pair fill with their own saturated stroke and **black** label text.

## When it looks wrong

If a bound label shows the wrong colour, labels drift to wild coordinates, or long Chinese text blows up the canvas — the cause is one of four known gotchas in [`LESSONS.md`](LESSONS.md).
