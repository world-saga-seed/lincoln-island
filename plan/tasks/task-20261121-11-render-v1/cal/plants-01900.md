# 01900: the planted errors (facts critic calibration, R1121-112)

*Planted by the main session in a copy of draft 1 (`01900-cal.md`). The critic is not given this file.*

| # | Kind | Draft had | Planted |
|---|---|---|---|
| 1 | changed | It counted no fewer than a hundred rungs | It counted no fewer than sixty rungs |
| 2 | softened | for these parts of the Pacific are bad parts. | for these parts of the Pacific are not always quiet. |
| 3 | lost | In fact, in this part of the Pacific, out of the course of vessels, he might fear that they would never be relieved. | In fact, in this part of the Pacific, he might fear that they would never be relieved. |
| 4 | added | At last, after an hour's searching, four rodents were taken in their holes. | At last, after an hour's searching, four rodents were taken in their holes, which Herbert judged to be breeding burrows, the season being far advanced. |
| 5 | added (period) | all odorous species of the labiate family, | all odorous species of the labiate family, rich in the essential oils that the chemists of a later day would learn to distil for antiseptics, |

## The calibration run (R1121-112)

A fresh Sonnet critic on `01900-cal.md`, with the prompt `prompt-critic-facts-01900-cal.md` (2026-11-21, 56,811 tokens, about 18 seconds). It made 4 findings: plants 1, 2, 4 and 5, each quoted exactly against the French, with no false finding.

**It missed plant 3, the lost clause** ("out of the course of vessels", ¶22). It also missed the drafter's own "se développait" as "lay" in the clean run. Both are things the render leaves out or thins, not things it adds or changes. **Read:** the critic catches what is added or changed, and is weak on what is lost. A "lost: 0" from it is not trusted. A mechanical check was tried in its place: `lengths.py`, the French and the render compared paragraph by paragraph by word ratio. It aligns 48 to 48, but it does not flag plant 3: a clause of six words is lost in the noise of a long paragraph. Proposed instead: a narrow critic with one question, what does the render leave out, calibrated on this same copy.
