---
description: China GB standard vs JIS, DIN, and EN battery standards — how GB/T 5008 model naming, CCA test basis, and sizing compare for the Chinese domestic market and cross-standard sourcing.
schema_type: TechArticle
date: 2026-09-08
---

# China GB Standard vs JIS, DIN, and EN

The Chinese domestic market runs on its own national standard — **GB/T 5008** for lead-acid starter batteries — and its model-naming and testing conventions differ from the JIS, DIN, and EN systems used across Japan, Asia, and Europe. For an OEM buyer or distributor who sources in China but sells into multiple markets, understanding the GB standard is the difference between an accurate cross-reference and a spec error.

This page covers how GB naming works, how GB test temperature and capacity rating compare to JIS/DIN/EN, and how to translate between them. See [Standards Comparison](../specs/standards-comparison.md) and [JIS vs DIN vs BCI](jis-din-bci.md) for the broader cross-standard picture.

## What GB/T 5008 Actually Is

GB/T 5008 is the Chinese national standard for *lead-acid starter batteries* (起动用铅酸蓄电池). It is issued and maintained by the Chinese administration for standards (SAC) and the electrical-equipment industry. The current widely-cited revision is:

- **GB/T 5008.1-2013** — *Lead-acid starter batteries — Part 1: Technical conditions and test methods.*
- **GB/T 5008.3-2023** — a later revision in the same series, implementing 2024-06-01.

The standard defines the technical specification and the test methods, including how nominal capacity and cold-cranking performance are measured. This is the reference point for the Chinese market precisely as JIS D 5301 is for Japan and EN 50342 is for Europe.

## GB Model Naming: Reading 6-QW-60

GB model designations encode the battery's structure in a short string. The most common form looks like `6-QW-60`, and it decomposes as follows:

| Segment | Meaning |
|---|---|
| `6` | Number of series cells (6 × 2V = 12V) |
| `Q` | 起动 — "starting" (the service type) |
| `W` | 免维护 — "maintenance-free" (sealed/VRLA, lead-calcium) |
| `60` | Nominal capacity in Ah (20-hour rate) |

So `6-QW-60` reads: a 12V, maintenance-free, 60 Ah starting battery. Omit the `W` (e.g. `6-QA-60`) and you have a wet, maintainable flooded unit. This is the same idea as JIS naming (`145G51` → performance rating + terminal/case code) but expressed through characters rather than numbers-plus-letters. See [Glossary](../glossary/index.md) for the term definitions.

## Test Temperature and CCA Basis

The single most important cross-standard trap is the cold-cranking test temperature, because CCA is not a universal number.

| Standard | CCA test temperature | Capacity rating basis |
|---|---|---|
| JIS (D 5301) | −15°C | 20-hour rate (C20) |
| DIN / EN (50342) | −18°C | 20-hour rate (C20) |
| SAE / BCI | −18°C | 20-hour rate / reserve capacity |
| GB (5008) | −18°C | 20-hour rate (C20) |

GB cold-cranking is measured at **−18°C**, aligning with DIN/EN/SAE rather than JIS's warmer −15°C. Practically, that means a GB-rated battery and a DIN/EN-rated battery of the same capacity are closer in CCA basis than either is to a JIS figure. A JIS CCA number will tend to read *higher* for the same physical battery than a GB/DIN number, simply because the test is run warmer. There is no safe universal multiplier — always compare within one standard. See [CCA Testing](../quality/cca-testing.md).

## Capacity Rating: C20 and the 20-Hour Rule

All four standards quote nominal capacity at the **20-hour rate (C20)** — the constant current a fully charged battery delivers over 20 hours before reaching the cut-off voltage (~10.5V for a 12V unit). This part is consistent across GB, JIS, DIN, and EN, which makes *capacity* the most portable figure when you translate between markets.

The catch is that some legacy and fleet documentation still quotes a **5-hour rate (C5)**, especially for Chinese domestic and some Asian references. Because a faster discharge returns a lower Ah number, C5 ≈ 0.8 × C20 as a rough guide. When a spec sheet doesn't state the rate, ask — a "60 Ah" number could be C20 or C5, and the difference is material. See [Capacity & Reserve](../quality/capacity-reserve.md).

## Dimensional and Terminal Conventions

GB does not impose a single group-size scheme the way JIS (N-series) or DIN (DIN88/DIN100) do. Instead, GB-compliant batteries are produced to match the vehicles and trays in the Chinese domestic fleet, which historically mixes Japanese, European, and domestic platforms. In practice:

- Many GB-market batteries share dimensions with **JIS** cases, because Japanese and domestic Chinese platforms overlap heavily.
- The **terminal** convention follows the use: JIS posts for Japanese-derived platforms, Euro recessed for European-derived ones.
- The GB standard defines **dimensional tolerances** (roughly ±2 mm on length/width, ±3 mm on height) rather than fixed sizes, so the same GB type can fit a range of trays.

This is why a Chinese-sourced battery is not automatically interchangeable with an "equivalent" JIS or DIN part — even when the Ah rating looks identical. Confirm case size, terminal type, and polarity against the target vehicle, not just the capacity. See [Standards Comparison](../specs/standards-comparison.md).

## The EFB Angle: China as a Start-Stop Market

China is now the world's largest single market for start-stop vehicles, and GB-compliant EFB and AGM batteries are a major domestic category. Start-stop cars cycle the battery thousands of times more than conventional vehicles, so the chemistry matters as much as the standard. A GB `6-QW` (maintenance-free flooded) is *not* a substitute for an EFB or AGM in a start-stop car. See [Battery Chemistry Comparison](battery-chemistry-comparison.md) for the construction differences and when each applies.

## Translating Between Standards

When cross-referencing a GB part to JIS, DIN, or EN, work through this order:

1. **Confirm the capacity rate** — C20 or C5? Normalise to C20.
2. **Confirm the CCA basis** — GB/DIN/EN are −18°C; JIS is −15°C. Don't treat the numbers as equal.
3. **Match the case size and terminal layout** — GB parts track JIS or Euro cases; verify against the tray before ordering.
4. **Confirm polarity** — GB, JIS, and DIN batteries each ship in right- and left-positive layouts.
5. **Confirm chemistry** — flooded, EFB, or AGM, per the vehicle's BMS.

The [battery model catalog](https://dingweibattery.com/data/) on the main website lists reference specifications across JIS and DIN/EN; use it as the anchor for cross-standard requests, then confirm the GB equivalent with the manufacturer.

## Source & Purchase

For OEM and private-label sourcing across GB, JIS, DIN, and EN specifications — including EFB and AGM chemistry for the Chinese start-stop market — [request a quote](https://dingweibattery.com/contact/) on the main website.
