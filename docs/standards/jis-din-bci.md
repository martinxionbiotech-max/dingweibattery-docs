---
description: JIS vs DIN vs BCI battery standards — how the three major standards differ in group sizing, CCA testing, and terminal conventions.
schema_type: TechArticle
date: 2026-09-08
---

# JIS vs DIN vs BCI

The three major battery standards — JIS, DIN, and BCI — serve different markets and use different conventions for group sizing, testing, and terminals. Knowing the difference prevents specification errors.

## Group Sizing

| Standard | Region | Group Size Example |
|---|---|---|
| JIS | Japan, Asia | N150, N200 |
| DIN | Europe | DIN88, DIN100 |
| BCI | North America | Group 24, 27, 31, 49 |

## CCA Testing

CCA is measured at different temperatures depending on the standard:

- **JIS** tests at −15°C
- **DIN** tests at −18°C
- **BCI/SAE** tests at −18°C

Because of the temperature difference, a JIS CCA and a DIN CCA are not directly comparable for the same battery. See [CCA Testing](../quality/cca-testing.md).

## Terminal Conventions

- **JIS** — typically smaller posts with distinct polarity conventions
- **DIN** — recessed terminals, standard European layout
- **BCI** — top posts or side terminals depending on group size

## Choosing the Right Standard

The correct standard is determined by your target market and the vehicles you serve:

- Selling into Japan/Asia → JIS
- Selling into Europe → DIN/EN
- Selling into North America → BCI/SAE

Always confirm the group size, terminal layout, and CCA test basis match your market before specifying. See the full [standards comparison](../specs/standards-comparison.md) for details.
