# Week 12: Capstone — private collateral eligibility

**Duration:** five learning days (2–3 hours each), one 120-minute mock exam, one catch-up day. Independent exercises; not official RareSkills bootcamp material.

## Required RareSkills articles

- [Circom language tutorial](https://rareskills.io/post/circom-tutorial)
- [Intermediate Signals and Sub-Component](https://rareskills.io/post/circom-intermediate-signals)
- [Public and Private Inputs](https://rareskills.io/post/circom-public-private-inputs)
- [How Tornado Cash Works](https://rareskills.io/post/how-does-tornado-cash-work)

## Specific YouTube videos

- [Workshop: Circom, SnarkJS and Solidity DApp](https://www.youtube.com/watch?v=1tw2wB5i9z8)
- [BattleZips: Solidity Verifier Integration](https://www.youtube.com/watch?v=zXHLIvIDO7w)

These are direct watch URLs for identifiable videos, not search pages. Videos are supplementary; prioritize the RareSkills reading.

## Day-by-day assignments

### Day 1

Write the threat model and specification: private amount A, private haircut H, public minimum T; constrain 0 ≤ H ≤ 10000 and bounds for A and T.

**Submission:** `solutions/week-12/day-1/` with notes, implementation, and tests. Record progress in `progress.csv`.

### Day 2

Implement circuit with integer semantics: eligible iff A*(10000-H) ≥ 10000*T; range-constrain values and multiplication to avoid finite-field wraparound. Define what the inequality means at equality.

**Submission:** `solutions/week-12/day-2/` with notes, implementation, and tests. Record progress in `progress.csv`.

### Day 3

Compile Circom; inspect constraints; generate valid and invalid witnesses including boundary cases, H=10000, T=0, and max configured amount.

**Submission:** `solutions/week-12/day-3/` with notes, implementation, and tests. Record progress in `progress.csv`.

### Day 4

Run snarkjs Groth16 setup, proof generation and verification with development-only ceremony material; export verifier and add Foundry integration tests.

**Submission:** `solutions/week-12/day-4/` with notes, implementation, and tests. Record progress in `progress.csv`.

### Day 5

Add nullifier or context-binding if the application needs one-time use, document replay protection and deployment assumptions, benchmark gas, write README demo and limitations.

**Submission:** `solutions/week-12/day-5/` with notes, implementation, and tests. Record progress in `progress.csv`.

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
