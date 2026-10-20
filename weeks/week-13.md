# Week 13 — Capstone: build

**Goal:** prove privately that a collateral position clears an eligibility threshold after a haircut, and verify it on-chain. Work in `capstone/`.

## The statement

Public: threshold `T`, a commitment `C`, and a context value `ctx` (e.g. hash of chain ID + verifier address + request ID).
Private: amount `A`, haircut `H` in basis points, and a random salt `s`.

The circuit proves:

1. `C = Poseidon(A, H, s)` — **the private data is bound to something real.** Without this line the prover can pick any A, and the proof means nothing. In a real system a custodian or the collateral contract publishes C.
2. `0 ≤ H ≤ 10000`
3. `A < 2^96` and `T < 2^96` (range checks; pick and justify your own bounds)
4. `floor(A × (10000 − H) / 10000) ≥ T`
5. `ctx` is a public signal so a proof can't be replayed in another context.

**Simplification you should prove and then use:** for integers X ≥ 0 and T, `floor(X / 10000) ≥ T` holds exactly when `X ≥ 10000·T`. So check `A·(10000 − H) ≥ 10000·T` with a comparator, and avoid in-circuit division entirely. Write the two-line proof in your spec.

## Day 1 — Spec and threat model
- Write `capstone/SPEC.md`: the statement above, every signal (public/private, bit-width), every constraint, and why the comparator bit-width is safe (largest possible value of each side vs the comparator's n).
- Write `capstone/THREAT_MODEL.md` using your Tornado notes from Week 11: what an attacker controls, what each public signal stops, what is out of scope (e.g. whether the custodian's commitment is honest).
- **Deliverable:** both files

## Day 2 — Circuit
- Write `capstone/circuits/eligibility.circom` using circomlib's `Poseidon`, `Num2Bits`, `LessEqThan` / `GreaterEqThan`.
- Count the constraints; you should be able to explain roughly where each one comes from.
- **Deliverable:** compiling circuit + constraint count in SPEC

## Day 3 — Witness tests
- Valid cases: H = 0, H = 10000 with T = 0, X exactly equal to 10000·T, large A near 2^96.
- Invalid cases: X one below 10000·T, H = 10001, A = 2^96, wrong salt, wrong commitment.
- Malicious cases: try to satisfy the circuit with an A that wraps around the field. Your range checks must stop it.
- **Deliverable:** `capstone/test/` with a script that runs every case and asserts the expected result

## Day 4 — Proof and verifier
- Generate the Groth16 setup, a proof for one valid case, and the Solidity verifier.
- Build `capstone/contracts/EligibilityGate.sol` that verifies a proof, checks `C` against a stored commitment, checks `ctx`, and records a nullifier so each eligibility proof is used once.
- **Deliverable:** contract + one passing Foundry test

## Day 5 — Integration
- Foundry tests: valid proof passes; each invalid witness can't produce a proof; malleated proof is rejected by the nullifier logic; wrong `ctx` fails; replay fails; public input ≥ r fails.
- **Deliverable:** green Foundry suite

## Day 6 — Checkpoint review (instead of an exam)
Give yourself 2 hours to review the capstone as if it were someone else's code: try to break it using every pitfall from Week 11. Log everything you find in `capstone/FINDINGS.md`. Fix in Week 14.

## Day 7 — Rest

## Exit criteria
- [ ] SPEC and THREAT_MODEL written before the code
- [ ] Circuit, witness tests and Foundry tests all pass
- [ ] Self-review findings logged
