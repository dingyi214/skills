#!/usr/bin/env python3
"""Restyle any .excalidraw to the marker style (palette-agnostic).

For each shape, snaps its colours to the nearest Excalidraw native pair
(saturated stroke + light same-hue fill), then forces the marker stroke /
text rules. Layout and text content are preserved.

Usage:
    python3 transform.py diagram.excalidraw [another.excalidraw ...]
"""
import json
import sys
import colorsys

# Excalidraw native pairs: (name, fill_light, stroke_saturated)
NATIVE = [
    ("red",    "#ffc9c9", "#e03131"),
    ("orange", "#ffd8a8", "#e8590c"),
    ("green",  "#b2f2bb", "#2f9e44"),
    ("cyan",   "#99e9f2", "#0c8599"),
    ("blue",   "#a5d8ff", "#1971c2"),
    ("purple", "#eebefa", "#9c36b5"),
    ("gray",   "#e9ecef", "#868e96"),
]
GRAY = NATIVE[-1]


def _rgb(hexstr):
    h = hexstr.lstrip("#")
    return (int(h[0:2], 16) / 255, int(h[2:4], 16) / 255, int(h[4:6], 16) / 255)


def _hsv(hexstr):
    return colorsys.rgb_to_hsv(*_rgb(hexstr))


# Precompute each coloured pair's hue angle (degrees). Gray handled separately.
_COLOURED = [
    (name, fill, stroke, _hsv(fill)[0] * 360)
    for name, fill, stroke in NATIVE[:-1]
]


def nearest_pair(color):
    """Return (name, fill, stroke) of the nearest native pair, or None."""
    if not color or color == "transparent":
        return None
    try:
        _, sat, _ = _hsv(color)
    except (ValueError, IndexError):
        return None
    if sat < 0.08:  # near-achromatic -> gray, regardless of hue
        return GRAY
    ang = _hsv(color)[0] * 360
    return min(
        _COLOURED,
        key=lambda p: min(abs(ang - p[3]), 360 - abs(ang - p[3])),
    )


def transform(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    els = data.get("elements", [])
    for e in els:
        t = e.get("type")
        if t in ("rectangle", "ellipse", "diamond"):
            bg = e.get("backgroundColor")
            has_fill = bool(bg) and bg != "transparent"
            pair = nearest_pair(bg) or nearest_pair(e.get("strokeColor"))
            if pair:
                if has_fill:
                    e["backgroundColor"] = pair[1]
                e["strokeColor"] = pair[2]
            elif not has_fill:
                e["strokeColor"] = "#000000"
            e["fillStyle"] = "solid"
            e["strokeWidth"] = 4
            e["strokeStyle"] = "solid"
            e["roughness"] = 0
            e["roundness"] = {"type": 3}
        elif t == "text":
            e["strokeColor"] = "#000000"
            e["fontFamily"] = 1
            e["roughness"] = 0
        elif t in ("arrow", "line"):
            e["strokeColor"] = "#000000"
            e["strokeWidth"] = 4
            e["strokeStyle"] = "solid"
            e["roughness"] = 0
            if t == "arrow":
                e["roundness"] = {"type": 2}
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)
    return len(els)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: transform.py <file.excalidraw> [...]", file=sys.stderr)
        sys.exit(2)
    for p in sys.argv[1:]:
        n = transform(p)
        print(f"restyled {p} ({n} elements)")
