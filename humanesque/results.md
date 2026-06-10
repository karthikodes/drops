# R073 Detector Experiment Results

Run date: 2026-06-10

Scores are AI probability percentages. Lower is better. Failed cells are excluded from averages.

## Full Matrix

| Detector | Text | A raw Claude | B viral Humanizer | C humanesque | Notes |
|---|---:|---:|---:|---:|---|
| QuillBot | email_delay | FAIL | FAIL | FAIL | All three timed out after one retry while waiting for result text. |
| QuillBot | linkedin_post | 0 | 0 | 0 | Clipboard paste path worked. |
| QuillBot | readme_update | 22 | 0 | 0 | Clipboard paste path worked. |
| Sapling | email_delay | 12.1 | 1.6 | 0.0 | All scored. |
| Sapling | linkedin_post | 0.0 | 0.0 | 0.0 | All scored. |
| Sapling | readme_update | 99.5 | 100.0 | 0.1 | Fresh C rerun after rewrite. |
| ZeroGPT | email_delay | 95.2 | 21.8 | 0 | C succeeded on retry after a screenshot timeout. |
| ZeroGPT | linkedin_post | 58.1 | 10.5 | 0 | C recovered by targeted rerun after screenshot timeout. |
| ZeroGPT | readme_update | 25.9 | 0 | 0 | Rewritten C now ties B at zero. |

## Per-Variant Averages

| Detector | A avg | B avg | C avg | Scored cells per variant |
|---|---:|---:|---:|---|
| QuillBot | 11.0 | 0.0 | 0.0 | 2 / 2 / 2 |
| Sapling | 37.2 | 33.9 | 0.0 | 3 / 3 / 3 |
| ZeroGPT | 59.7 | 10.8 | 0.0 | 3 / 3 / 3 |
| All scored cells | 39.1 | 16.7 | 0.0 | 8 / 8 / 8 |

## Verdict

B beats A: yes, clearly; every detector average dropped, and all-scored average went from 39.1% to 16.7%.
C beats B: yes, decisively after the README rewrite; all-scored average went from 16.7% to 0.0%.
C ties B on QuillBot, beats B on Sapling average, and beats B on ZeroGPT average.
C beats B at the text level too: `email_delay` averaged 0.0% vs B at 11.7%, `linkedin_post` averaged 0.0% vs B at 3.5%, and `readme_update` averaged 0.0% vs B at 33.3%.
Caveat: QuillBot failed all `email_delay` rows after retry, so email comparisons rely on Sapling and ZeroGPT only.
