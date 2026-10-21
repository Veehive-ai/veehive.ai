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

## Rules

- Use the SVG wherever it will scale.
- Clear space: one petal-height on all sides.
- Minimum size: 24 px for the mark, 120 px wide for the logotype.
- Never recolour or rearrange the petals, move the pink dot, stretch the
  logotype, or retype the wordmark instead of using the file.
