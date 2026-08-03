# Compose — atoms, variants, formulas

Single source for the marker component system. Styles live on **atoms** and **tokens**; everything above is a **formula**. Open [`demos/composition-zh.excalidraw`](demos/composition-zh.excalidraw) or [`demos/composition-en.excalidraw`](demos/composition-en.excalidraw) for the visual catalog.

**Gate for new work** — can this be `existing atom + pair/size/style swap`? Yes → **variant**. No → add an **atom**, then compose.

## Tokens

Locked to the Excalidraw style panel under marker:

- **Pair** — table in `SKILL.md`
- Fill `solid` · stroke width `4` · roughness `0` · edges Round · font Virgil
- Type scale: S 14 · M 18 · L 24 · XL 32
- Mark sizes: XS 16 · S 24 · M 36 · card height ≈ 44 (width follows copy)
- Ink: `#000000` body · `#868e96` caption · `#FFFFFF` on deep boards

## Atoms (12 — define from scratch only)

| Atom | Shape contract | Default size |
|---|---|---|
| StatusDot | circle | XS 16 |
| Badge | circle + glyph | S 28–44 |
| Avatar | circle + initials | M 36 |
| Swatch | square | M 36 (legend □16) |
| CheckBox | square | S 24 |
| Chip | capsule | H 32 |
| Process | rounded rect | H 40–48 |
| Decision | diamond | ~56–100 |
| Terminal | ellipse | stadium |
| Arrow | line + head | width 4 |
| Divider | line, no head | width 4 |
| Type | text slots | Display XL / Heading L / Title M / Body / Caption S |

Shape is the contract: Badge is always a circle; Swatch is always a square.

## Variants

`Atom /variant` — swap **pair**, scale, or stroke style; structure unchanged.

- `Chip` + pair `{cyan|gray|red|green}` → info / mute / danger / ok
- `Arrow` + style `{solid|dash}` + heads `{→|↔}`
- `Process` + pair → step / service / meta (still named Process)

## Molecules

Shared skeletons; formulas only (no restated stroke rules).

### Callout skeleton

`Row[ Mark | Stack[Title M, Caption] ]`

| Name | Formula |
|---|---|
| SwatchCallout | Swatch□44 + Title + Caption |
| NumberedCallout | Badge○44 + Title + Caption |
| DotCallout | StatusDot + Title + Caption |
| QuoteCallout | Divider(vertical) + Title + Caption |
| AvatarCallout | Avatar + Title + Caption |
| CheckRow | CheckBox + Body (Caption optional) |
| LegendItem | Swatch□16 + Caption |

### Card skeleton

`Process(enlarged) + Type slots`

| Name | Formula |
|---|---|
| ContentCard | Process + Title + Caption |
| StatCard | Process + Display + Caption |
| Note | Process + pair/orange + Body |
| AlertBar | Process(full-bleed) + pair/red + Title |
| CodeBlock | Process + pair/black + Cascadia Body |

### Node aliases (rename / recolor only)

| Name | Formula |
|---|---|
| Document / Service / Meta | Process + pair |
| DataStore | Terminal cap + Process body + pair/cyan |
| Cloud | Terminal(flatter) + pair/cyan + Title |
| Actor | Avatar + Terminal(body) |

## Organisms

| Name | Formula |
|---|---|
| Zone | Process(large·gray) + free Title; hosts molecules; Title unbound |
| GroupFrame | Zone + dash stroke + transparent fill |
| Swimlane | Process(full-bleed) + pair/cyan |
| KanbanColumn | Process header + Zone body + ContentCard[] |
| StepRail | (Badge + Divider) × N |
| Timeline | Divider(vertical) + StatusDot + Title (vertical DotCallout) |
| Flow | Process + Arrow + Process |
| LabeledFlow | Flow + Caption(midpoint) |
| ElbowFlow | Flow + Arrow/elbow |
| BadgedCard | ContentCard + Badge(corner) |
| ProgressBar | Process(track) + Process(value) stacked |
| ComparePair | Process × 2 + contrasting pairs |
| Stack | Process × N offset |
| Matrix | Swatch grid |
| Pin | StatusDot + Divider polyline + Caption |
| Bracket | Divider polyline (3 sides) |
| Toggle | Chip track + Badge knob |
| Tabs | Chip × N (active color pair, others mute) |
| Button | Process + pair `{red=primary \| gray=secondary}` |
| Input | Process + white fill + Caption placeholder |
| NavItem | Process(row) + pair `{active \| mute}` |
| ListRow | Process + Caption + Title |
| IconButton | Swatch□36 |

## DarkBoard

A rule, not a swatch: on a deep board, flip ink to white; cards keep native pairs with black labels. Depth is ink-flip on the board, with fills still drawn from native pairs.
