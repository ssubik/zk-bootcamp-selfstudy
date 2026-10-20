# ZK Bootcamp Self-Study

A 14-week, hands-on path from modular arithmetic to a production-style Groth16 application verified on Ethereum, plus 2 optional weeks on PLONK and KZG. Built on the public [RareSkills ZK Book](https://rareskills.io/zk-book); not affiliated with RareSkills. Exercises and exams are original.

**Start here:** [CURRICULUM.md](CURRICULUM.md) — the plan, the schedule, and every verified reading and video. Daily instructions are in [`weeks/`](weeks/).

## How it works

- **5 study days + 1 exam + 1 rest** per week, about 2–2.5 hours a day.
- Weeks 1–7 have Python exercise stubs in `src/` with tests in `tests/`. You build a finite field, groups, elliptic curves, R1CS, polynomials and a QAP converter from scratch; Week 9 combines them into your own Groth16.
- Weeks 10–12 move to Circom, snarkjs and Foundry, with a full week on underconstrained-circuit attacks.
- Weeks 13–14 are the capstone.

## Setup

```
pip install -r requirements.txt      # py_ecc, used from Week 3
python3 -m unittest tests.test_field -v   # Week 1
```

Run only the current week's tests (`tests.test_algebra`, `tests.test_ec`, `tests.test_r1cs`, `tests.test_poly`, `tests.test_qap`). Later weeks fail until you implement them. Foundry is first used in Week 4; Circom and snarkjs in Week 10.

Put your own work under `solutions/week-NN/` and log each day in `progress.csv`.

## Capstone

Prove privately that a committed collateral amount `A` and haircut `H` (basis points) satisfy `floor(A × (10000 − H) / 10000) ≥ T` for a public threshold `T`, and verify the proof in a Solidity contract with nullifier-based replay protection. Full spec in [week 13](weeks/week-13.md). Educational, not production-ready.
