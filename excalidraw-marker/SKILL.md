---
name: excalidraw-marker
description: >-
  Apply the **marker** look and **compose** Excalidraw diagrams from **pair**-colored
  **atoms**. Use when drawing or restyling a `.excalidraw`, or when the user mentions
  marker 风, excalidraw 风格 / 上色, 重画 / 重写 .excalidraw, or house-style diagrams.
---

# Marker

A diagram is **marker** when every filled shape carries a native **pair** (saturated stroke + same-hue light fill), strokes are extra-bold solid rounded (`strokeWidth: 4`, `roughness: 0`, `roundness: {type: 3}`, `fillStyle: solid`), ink is pure black on light (white on a deep board), and type is Virgil (`fontFamily: 1`). Lines and arrows use the same ink and width; arrows use `roundness: {type: 2}`.

**Compose** — build the scene from the twelve **atoms** and the formulas in [`COMPONENTS.md`](COMPONENTS.md). A new need that is “same atom, different pair/size” is a **variant**, not a new component. Labels on nodes use the shape’s bound `text` (auto-centred); titles on large boards stay free-standing.

Visual catalog: [`demos/composition-zh.excalidraw`](demos/composition-zh.excalidraw) · [`demos/composition-en.excalidraw`](demos/composition-en.excalidraw).

## Drawing a new diagram

1. Plan the layout, then place **atoms** / composed formulas from [`COMPONENTS.md`](COMPONENTS.md) — pick a **pair** per role, keep the diagram to 3–4 hues.
2. After bound labels exist, set each bound text’s `strokeColor` to `#000000` (they inherit the shape stroke by default).
3. **Completion criterion** — every rectangle / ellipse / diamond shows a native pair; every text is `#000000` or `#FFFFFF`; every stroke is width `4` · solid; every composed block matches a formula in `COMPONENTS.md` (no one-off restated styles).

## Restyling an existing diagram

```bash
python3 transform.py path/to/diagram.excalidraw
```

Snaps colours to the nearest native **pair** and forces marker stroke / text rules; layout and copy stay.

**Completion criterion** — list distinct `backgroundColor` / `strokeColor` values; every coloured fill/stroke is in the pair table below (or ink black/white); every stroke is width `4` · solid.

## Pairs

| stroke | fill | feel |
|---|---|---|
| `#e03131` | `#ffc9c9` | error / critical |
| `#e8590c` | `#ffd8a8` | async / event |
| `#2f9e44` | `#b2f2bb` | success / healthy |
| `#0c8599` | `#99e9f2` | data / store |
| `#1971c2` | `#a5d8ff` | primary / link |
| `#9c36b5` | `#eebefa` | service / middleware |
| `#868e96` | `#e9ecef` | note / secondary / board |
| `#1e1e1e` | `#ffffff` | default text / border |

On a deep board, flip ink to white; cards on that board still use a light **pair** with **black** labels. Express depth by flipping ink on native pairs.

## When it looks wrong

Diagnose by symptom in [`LESSONS.md`](LESSONS.md) (bound-label colour, doubled labels, Chinese width blow-up, mermaid label drift).
