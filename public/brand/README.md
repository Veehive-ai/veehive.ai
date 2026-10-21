# Veehive brand kit

Everything needed to use the Veehive identity correctly. Open
`guidelines/veehive-brand-kit.html` in a browser for the full guide.

## Folders

| Path | Contents |
|---|---|
| `logo/` | Full logotype, light and dark. SVG + PNG at 512 / 1024 / 2048 px. |
| `mark/` | Mark on its own. SVG + PNG at 256 / 512 / 1024 px. |
| `favicons/` | Seven product marks. SVG + 32 / 64 / 192 px PNG each. |
| `fonts/Manrope/` | Variable font 300–800, with OFL licence. |
| `fonts/IBMPlexSans/` | Regular, Medium, SemiBold, Bold, with OFL licence. |
| `loaders/` | The six loading spinners, plus the padded marks they animate. |
| `logo/products/` | A logotype per product, dark and white text. SVG plus PNG at 96 and 192 px tall. |
| `mascots/` | A bee per product, plus the house bee. 256 px PNG. |
| `business-card/` | Card artwork, front and back, with the print-ready PDF. |
| `signature/` | The email signature, with a copy button and paste instructions. |
| `guidelines/` | The brand guide. |

## Motion

The mark is radially symmetric, so it rotates about its own centre as the
loading state. Six CSS-only timings, no JavaScript:

| Class | Timing |
|---|---|
| `.veehive-loader` | 1.2s linear — the default |
| `.veehive-loader-pulse` | spin + breathe |
| `.veehive-loader-slow` | 2.5s cubic-bezier |
| `.veehive-loader-fast` | 0.6s linear |
| `.veehive-loader-ease` | 1.5s ease-in-out |
| `.veehive-loader-flip` | 1.5s 3D rotateY |

Spin the padded mark, not the plain one — the padding stops the petals
clipping at the corners. Always pair it with a
`prefers-reduced-motion: reduce` rule that sets `animation: none`.
Open `loaders/index.html` to see all six.

## Palette

| Product | Primary |
|---|---|
| Mpliphi | `#2C573E` |
| HiveStudio | `#7C3AED` |
| SnapaPro | `#DC2626` |
| HiveLink | `#2563EB` |
| HiveMind | `#FFB020` |
| HiveDocs | `#0D9488` |
| HiveFront | `#EC4899` |

The six product colours sit in the mark's six petals, in a fixed
arrangement. HiveFront's pink is also the logotype accent — the dot over
the final "i" in Veehive.ai.

Wordmark is `#334155` on light grounds, `#FFFFFF` on dark.

## Typography

- **Manrope ExtraBold (800)** — the logotype and all headings.
  The logotype is set at a tracking of −4.07 per gap.
- **IBM Plex Sans** — body copy, interface text, long-form.

Both are SIL Open Font License; the licences ship beside the fonts.

## Product logotypes

Each product sets its own name beside the mark in its own colour, on the
same geometry as Veehive.ai: Manrope ExtraBold, cap height 80.64 on a
105.32 baseline, the mark at 0.9 scale, and the same gap from mark to
first letter. The name is never set in another weight and never in the
product colour — the mark carries the colour, the name stays neutral
(`#334155` on light, `#FFFFFF` on dark).

| Product | Colour |
|---|---|
| Mpliphi | `#2C573E` |
| SnapaPro | `#DC2626` |
| HiveStudio | `#7C3AED` |
| HiveLink | `#2563EB` |
| HiveMind | `#FFB020` |
| HiveDocs | `#0D9488` |
| HiveFront | `#EC4899` |
| VeehiveLabs | `#E8BB30` |

Every product mark also spins, using the same loader classes — a
product's own colour carries its loading state.

## Mascots

Every product has a bee, and every bee wears its product's colour on the
wings. They carry the warmth the mark deliberately doesn't — use them on
merch, in slides and anywhere the audience is people rather than
procurement. Never on a legal page, a certificate or a contract, and
never in place of the mark as an app icon.

| Bee | Product | Colour |
|---|---|---|
| ND | Mpliphi | `#2C573E` |
| Taj | SnapaPro | `#DC2626` |
| Chaks | HiveStudio | `#7C3AED` |
| AK | HiveLink | `#2563EB` |
| Mira | HiveMind | `#FFB020` |
| Dex | HiveDocs | `#0D9488` |
| — | HiveFront | `#EC4899` |
| — | Veehive (house) | `#334155` |

HiveFront's and the house bee are unnamed so far.

## Stationery and merch

The business card is 3.5 x 2 in at 300 dpi, set in
`business-card/card.html` — edit the HTML and print to PDF at that size
with margins off, rather than rebuilding it in a layout tool.

On cloth there are two placements and only two:

- **Full logotype**, centred on the chest.
- **Mark alone**, at the left chest (the wearer's left, so image-right on
  a front view), about a hand's width below the shoulder seam.

White logotype on anything darker than the mid-grey, dark logotype on
anything lighter. No drop shadow, no outline to rescue a difficult
colour — change the garment colour instead. Below about 60 mm wide,
embroidery loses the pink dot over the final i: print it, or use the
mark on its own.

## Rules

- Use the SVG wherever it will scale.
- Clear space: one petal-height on all sides.
- Minimum size: 24 px for the mark, 120 px wide for the logotype.
- Never recolour or rearrange the petals, move the pink dot, stretch the
  logotype, or retype the wordmark instead of using the file.
