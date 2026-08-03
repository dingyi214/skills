# Marker style — when it looks wrong

Four gotchas account for almost every breakage. Diagnose by symptom, apply the fix.

## Bound label text is the wrong colour

A shape's bound `text` inherits the shape's `strokeColor` by default — a blue-stroked card renders blue text, not the black you wanted.

**Fix** — after creating bound labels, find them (they carry a `containerId`) and set each one's `strokeColor`:

```bash
npx -y mcp-excalidraw-server query --type text   # spot those with containerId
npx -y mcp-excalidraw-server apply - <<'EOF'
{ "update": [ {"id":"<bound-text-id>","set":{"strokeColor":"#000000"}} ] }
EOF
```

## Bound labels doubled

The Excalidraw frontend's auto-sync sometimes duplicates every bound text — two text elements sharing one `containerId`, rendered on top of each other.

**Fix** — `query --type text`, find the duplicate IDs (same `containerId`), delete one of each pair with `delete <id>`.

## Long Chinese text explodes the canvas

Excalidraw will not wrap Chinese to a text element's `width`. A long single line stretches into one ultra-wide line and blows the canvas out.

**Fix** — break every long label manually with `\n`, and set the element's `width` to its longest line.

## Mermaid-imported arrow labels drift negative

Free-text labels that arrived via `mermaid` conversion get pushed to negative x by auto-sync, carving a giant left margin and separating the label from its arrow.

**Fix** — delete the drifted labels and recreate them as fresh free text (new IDs do not inherit the drift). Mermaid conversion also does not honour `<br>` reliably — use real `\n` and single-line labels in the mermaid source.
