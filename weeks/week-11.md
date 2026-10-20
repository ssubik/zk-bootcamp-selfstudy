# Week 11: Solidity Groth16 verification

**Duration:** five learning days (2–3 hours each), one 120-minute mock exam, one catch-up day. Independent exercises; not official RareSkills bootcamp material.

## Required RareSkills articles

- [Groth16 Explained](https://rareskills.io/post/groth16)
- [Bilinear Pairings](https://rareskills.io/post/bilinear-pairing)
- [Public and Private Inputs](https://rareskills.io/post/circom-public-private-inputs)

## Specific YouTube videos

- [BattleZips: Zero Knowledge Tutorial #1 — Solidity](https://www.youtube.com/watch?v=zXHLIvIDO7w)

These are direct watch URLs for identifiable videos, not search pages. Videos are supplementary; prioritize the RareSkills reading.

## Day-by-day assignments

### Day 1

Inspect Groth16 public-input verification and explain how public signals are bound to the verifier key.

**Submission:** `solutions/week-11/day-1/` with notes, implementation, and tests. Record progress in `progress.csv`.

### Day 2

Read EIP-196 and EIP-197; annotate ECADD, ECMUL and pairing precompile usage in generated Solidity.

**Submission:** `solutions/week-11/day-2/` with notes, implementation, and tests. Record progress in `progress.csv`.

### Day 3

Create a minimal Circom circuit with one private witness and one public output; compile, generate witness and proof with snarkjs.

**Submission:** `solutions/week-11/day-3/` with notes, implementation, and tests. Record progress in `progress.csv`.

### Day 4

Export the Solidity verifier and call it from a Foundry test. Confirm valid proof passes and wrong public signal fails.

**Submission:** `solutions/week-11/day-4/` with notes, implementation, and tests. Record progress in `progress.csv`.

### Day 5

Add negative tests: tampered proof, mismatched public input, replay in an application context, and field-boundary inputs. Document proof validity versus application authorization.

**Submission:** `solutions/week-11/day-5/` with notes, implementation, and tests. Record progress in `progress.csv`.

### Day 6 — Timed mock exam (120 minutes, 100 points)

**Theory (30):** Explain the Groth16 verifier pairing equation and public input binding (Week 11), or formalize the capstone's integer inequality and bounds (Week 12).

**Coding (50):** Produce a fresh proof-verification scenario with 3 valid/boundary tests and 3 invalid tests; supply reproducible commands and results.

**Debugging (20):** Find and repair an underconstraint, missing range bound, public-input mismatch, or replay weakness; explain whether it is a proof-system or application-layer issue.

Pass ≥75; distinction ≥90. Save the attempt and a self-assessment; do not assume a passing grade without running the tests.

### Day 7 — Catch-up and retrospective

## Exit checklist

- [ ] Read the linked RareSkills articles
- [ ] Watch and summarize the linked videos
- [ ] Commit source, test vectors, and reproducible commands
- [ ] Demonstrate negative and boundary tests
- [ ] Record mock exam score and remaining questions

**Security:** Educational examples only. A valid proof does not by itself establish ownership, authorization, freshness, or replay protection.
