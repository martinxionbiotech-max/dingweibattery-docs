---
description: AGM vs EFB vs flooded vs lead-calcium vs lead-antimony — a comparison of automotive lead-acid battery chemistries, construction, cycling, cost, and when to choose each.
schema_type: TechArticle
date: 2026-09-08
---

# Battery Chemistry Comparison: AGM vs EFB vs Flooded vs Lead-Calcium vs Lead-Antimony

Not all lead-acid batteries are the same chemistry. "Lead-acid" is the family name; inside it sit several distinct constructions — **AGM**, **EFB**, **conventional flooded**, and two grid-alloy routes, **lead-calcium** and **lead-antimony** — each with different cycling behaviour, water consumption, cost, and failure modes. Picking the wrong one for a start-stop car, a deep-cycle install, or a fleet truck costs money in early replacement.

This page maps the differences so you can specify the right chemistry the first time. For how these chemistries map onto specific standards and group sizes, see [JIS vs DIN vs BCI](jis-din-bci.md) and the [battery model catalog](https://dingweibattery.com/data/).

## The Two Axes: Construction vs Grid Alloy

It helps to separate two things that get conflated:

1. **Construction** — how the electrolyte is held: flooded (liquid), EFB (liquid + enhanced plate), or AGM (absorbed in glass mat).
2. **Grid alloy** — what the plate grids are made from: lead-calcium or lead-antimony.

These two axes are independent. A flooded battery can be lead-calcium *or* lead-antimony; an AGM or EFB is almost always lead-calcium. Most of the confusion in spec sheets comes from mixing the two.

## Construction Types Compared

| Feature | Flooded (wet) | EFB | AGM |
|---|---|---|---|
| Electrolyte | Free liquid | Liquid, enhanced plates | Absorbed in glass mat |
| Maintenance | Check/refill water | Occasional | None (sealed) |
| Cycle life | Low | ~2× flooded | High (high-cycle) |
| Charge acceptance | Standard | Faster | Fastest |
| Vibration resistance | Low–moderate | Improved | High |
| Start-stop compatible | No | Yes | Yes |
| Cost | Lowest | Mid | Highest |
| Typical service life | 3–5 years | 5–7 years | 6–8 years |

Sources: battery-industry technical literature; see [CCA Testing](../quality/cca-testing.md) for measurement context.

### Conventional Flooded

The oldest and cheapest form. Liquid sulfuric acid surrounds the plates, water is lost through normal operation, and the user tops up with distilled water. Flooded batteries are fine for standard starting duty with a healthy alternator, but they dislike deep discharge and repeated cycling.

- Pros: lowest up-front cost, widely available, fully recyclable.
- Cons: needs water top-up, shorter cycle life, not suited to start-stop or deep-cycling.

### EFB (Enhanced Flooded Battery)

An improved flooded design aimed at entry-level start-stop cars. It keeps the liquid electrolyte but reinforces the plates — a fibre/polymer scrim on the positive plate and carbon additives on the negative — to survive the far higher cycling that engine start-stop imposes.

- ~2× the cycle life of a standard flooded unit, at a fraction of AGM's cost.
- Best value for start-stop vehicles that don't need AGM's extreme performance.

### AGM (Absorbent Glass Mat)

The electrolyte is absorbed into a fibreglass mat, making the cell effectively "dry" and spill-resistant. AGM accepts charge faster, cycles deeper, and shrugs off vibration — the reason it's the default for start-stop luxury cars, off-road, marine, and backup applications.

- Highest performance and longest life, highest price.
- Spill- and vibration-resistant; ideal where the battery is mounted in-cabin or at odd angles.

For a dedicated breakdown of EFB versus AGM in a start-stop context, see the [GB standard comparison](gb-vs-jis-din-en.md) section on the Chinese domestic market, which is the world's largest single market for EFB.

## Grid Alloys: Lead-Calcium vs Lead-Antimony

The plate grid — the conductive lattice that holds the active material — is alloyed to add strength. The two dominant alloys behave very differently.

| Feature | Lead-Calcium | Lead-Antimony |
|---|---|---|
| Water loss | Very low | Higher |
| Self-discharge | Low | Higher |
| Maintenance | Maintenance-free capable | Needs periodic water top-up |
| Deep-cycle tolerance | More vulnerable to grid corrosion | More tolerant |
| Gassing / grid growth | Lower | Higher |
| Typical use | Sealed, MF, AGM, EFB | Traditional flooded, industrial/deep-cycle |

Sources: lead-acid battery technical references and manufacturer datasheets.

- **Lead-calcium** grids lose almost no water, which is what makes "maintenance-free" (免维护) batteries possible. Almost every AGM, EFB, and sealed flooded battery is lead-calcium. The trade-off: calcium grids are more prone to corrosion under sustained deep cycling.
- **Lead-antimony** grids are tougher under deep discharge and repeated cycling but consume water and self-discharge faster, so they need periodic top-up. They persist in traditional wet batteries and heavy industrial/stationary service.

The practical takeaway: "maintenance-free" is not a separate chemistry — it's a *property* of lead-calcium grid construction. When a Chinese-language datasheet labels a battery 免维护, it means lead-calcium, sealed/VRLA construction.

## Which Should You Choose?

- **Standard car, budget-driven** → conventional flooded (lead-calcium for low water loss).
- **Entry start-stop, cost-conscious** → EFB.
- **Start-stop luxury, high load, in-cabin/odd-angle mount** → AGM.
- **Deep-cycle / industrial / stationary** → lead-antimony flooded for tolerance, or AGM if sealed is required.
- **Heavy truck / bus / genset starting** (the N150/N200 class) → high-capacity maintenance-free flooded (lead-calcium); see [145G51 (N150)](../specs/jis-145g51.md) and [190H52 (N200)](../specs/jis-190h52.md).

## Why It Matters for Sourcing

The chemistry decision is downstream of the vehicle's charging system and duty cycle, not something you can swap freely. A start-stop car fitted with a conventional flooded battery fails early and can trigger the BMS to disable the start-stop function; an AGM fitted where a standard flooded was specified is money wasted. Confirm the chemistry the vehicle expects, then specify it explicitly in the RFQ. See the [RFQ guide](../oem/rfq-guide.md) for how to state chemistry, CCA basis, and terminal layout unambiguously.

## Source & Purchase

For OEM and private-label sourcing across flooded, EFB, and AGM chemistries with full analytical documentation, [browse the complete battery catalog](https://dingweibattery.com/data/) on the main website.
