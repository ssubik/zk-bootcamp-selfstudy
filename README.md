# ZK Bootcamp Self-Study

Independent **12-week, 6-day/week** hands-on study plan inspired by the public [RareSkills ZK Book](https://rareskills.io/zk-book). Not affiliated with RareSkills; exercises and mock exams are original, not their private bootcamp material.

**Target:** 2–3 hours per study day. Days 1–5: 30m review, 45m reading/video, 60–90m coding, 15m notes. Day 6: timed mock exam. Day 7: rest/catch-up.

## Start with the curated curriculum

**[Daily RareSkills reading assignments and exam specifications](CURRICULUM.md)** are the current source of truth. The older weekly files are supplementary and contain outdated generic video-search prompts; those are not verified recommendations.

## Curriculum

- [Week 01: Finite fields](weeks/week-01.md) — modular arithmetic, inverses, Fermat's theorem, field axioms, roots of unity
- [Week 02: Linear algebra and arithmetic circuits](weeks/week-02.md) — vectors, matrices, arithmetic gates, witness assignment, constraint systems
- [Week 03: R1CS](weeks/week-03.md) — rank-1 constraints, witness ordering, public inputs, satisfiability, soundness pitfalls
- [Week 04: Elliptic curves](weeks/week-04.md) — groups, point addition, scalar multiplication, subgroup order, BN254
- [Week 05: Pairings](weeks/week-05.md) — G1 G2 GT, bilinearity, pairing checks, BN254 precompiles
- [Week 06: Polynomial arithmetic](weeks/week-06.md) — Lagrange interpolation, polynomial division, vanishing polynomial, FFT intuition
- [Week 07: QAP](weeks/week-07.md) — R1CS to QAP, witness polynomials, divisibility, quotient polynomial
- [Week 08: Trusted setup and Pinocchio](weeks/week-08.md) — toxic waste, powers of tau, knowledge assumptions, Pinocchio overview
- [Week 09: Groth16](weeks/week-09.md) — setup, proof elements, verifier pairing equation, completeness and soundness
- [Week 10: Circom and snarkjs](weeks/week-10.md) — signals, templates, component constraints, witness generation, test vectors
- [Week 11: Ethereum verification](weeks/week-11.md) — BN254 precompiles, Solidity verifier, gas, public signals, replay resistance
- [Week 12: Capstone and review](weeks/week-12.md) — private collateral eligibility proof, threat model, integration tests, end-to-end demo

## Start

```bash
python3 -m unittest discover -s tests -v
```

Implement functions in `src/field.py`, then run tests. Work through each weekly guide and record results in `progress.csv`. The mock exams use 100 points: 30 conceptual, 50 programming, 20 explanation/debugging; pass at 75, distinction at 90. No exam answers are included inline, to preserve the self-assessment.

## Reading & video references

- [RareSkills ZK Book](https://rareskills.io/zk-book)
- [RareSkills blog](https://rareskills.io/blog)
- [ZK Whiteboard Sessions](https://www.youtube.com/results?search_query=ZK+Whiteboard+Sessions)
- [Circom documentation](https://docs.circom.io/)
- [snarkjs](https://github.com/iden3/snarkjs)
- [Ethereum EIP-196](https://eips.ethereum.org/EIPS/eip-196), [EIP-197](https://eips.ethereum.org/EIPS/eip-197)

Video links in weekly guides are **topic searches**, not claims that a particular recording was verified. Read the relevant sections of the RareSkills book by topic; section names and ordering may change.

## Capstone

Implement a demo proving privately that a collateral amount and haircut satisfy a public minimum eligibility threshold. Specify exactly which values are private/public, ensure witness binding, test boundary and malicious cases, generate a Groth16 proof using Circom/snarkjs, and verify it in Solidity. This is educational, not production-ready.
