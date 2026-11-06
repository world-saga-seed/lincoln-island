# 12 Accept and release

*Refinement. Add this when a volume is accepted, and once per volume before release.*

**When:** when a volume has been read (stage 10) and the writer accepts it; then once per volume, before release.

**Uses:** [accepting a volume](../../plan/workflows/retrospective.md#accepting-a-volume), [retire](../../plan/workflows/retire.md), [publication](../../plan/workflows/publication.md) (once per volume, before release).

**What happens:** the volume is accepted, its working papers shrink and retire, and the next horizon is set; before release, the publication checks ([publication](../../plan/workflows/publication.md)).

**Done when:** the volume's chapters are accepted in `plan/state.md`, its papers retired, and the release checks passed.
