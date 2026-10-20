# Week 14 — Capstone: harden, final exam, write-up

**Goal:** finish the capstone to a standard you'd show an employer or co-founder, prove to yourself you can do the whole pipeline without notes, and see where Groth16 sits in the wider field.

**Video:** [ZKP MOOC Lecture 2: Overview of Modern SNARK Constructions](https://www.youtube.com/watch?v=bGEXYpt3sj0) (Day 4)

## Day 1 — Fix findings
- Fix everything in `capstone/FINDINGS.md`, each with a regression test.

## Day 2 — Invariants
- Write Foundry invariant tests for `EligibilityGate`: no nullifier is ever accepted twice; no state change happens on a failed verification; the stored commitment can only change through its intended path.
- **Deliverable:** invariant suite passing

## Day 3 — Write-up
- `capstone/README.md`: the problem, the statement, design decisions (why the division-free comparison, why those bit-widths, why Poseidon), the threat model summary, test coverage, gas cost, and known limitations (trusted setup, honest commitment, educational only).
- **Deliverable:** a README someone else could follow

## Day 4 — The bigger picture
- Watch the Berkeley Lecture 2. Write one page placing Groth16 among other SNARKs: trusted setup per circuit vs universal setup, proof size, verifier cost, prover cost. Where would PLONK or a STARK be a better choice for an institutional settlement system?
- **Deliverable:** `solutions/week-14/landscape.md`

## Day 5 — Review weak spots
- Re-read your lowest-scoring weeks in `progress.csv` and redo their exams' coding sections.

## Day 6 — Final exam (180 min, closed notes)
1. **Theory (30):** Walk through the whole pipeline for `out = x²·y + 3`: flattening, R1CS, QAP, setup, proof, verification equation. Explain where Schwartz–Zippel, the pairing and the trusted setup each come in.
2. **Coding (50):** Write a fresh Circom circuit for "a private value is in a public Merkle tree of depth 4 and is ≥ a public minimum", with a Solidity verifier and Foundry tests (3 valid, 3 invalid).
3. **Debugging (20):** Review a provided circuit + contract pair with 3 planted bugs (one in constraints, one in public-input handling, one in replay protection). Find and fix them.

Pass 75; distinction 90. If you pass, you have covered what this course set out to teach.

## Day 7 — Rest

## Exit criteria
- [ ] Capstone complete with README, threat model and invariant tests
- [ ] Final exam passed
- [ ] Decide whether to continue to Weeks 15–16
