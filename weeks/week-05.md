# Week 5 — R1CS and a first ZK proof from R1CS

**Goal:** turn any small program into a rank-1 constraint system by hand, and see why "encrypted R1CS" works but is neither succinct nor sound enough on its own.

**Reading:** [R1CS](https://rareskills.io/post/rank-1-constraint-system) · [Building a ZK proof from an R1CS](https://rareskills.io/post/r1cs-zkp)
**Video:** [ZK-LDN 0x01: Designing efficient R1CS circuits — Daira Hopwood](https://www.youtube.com/watch?v=Uug5p05_wqs) (Day 4)
**Code:** `src/r1cs.py` → `python3 -m unittest tests.test_r1cs -v`

## Day 1 — From program to constraints
- Read the first half of *R1CS*.
- By hand, flatten these into constraints of the form `left × right = output`: (a) `out = x³ + x + 5`, (b) `out = x·y·z`, (c) `out = 3x²y + 5xy − x − 2y + 3`. Count the constraints for each; aim for the minimum.
- **Deliverable:** `solutions/week-05/flatten.md`

## Day 2 — Matrices and the witness vector
- Finish *R1CS*.
- Implement `is_satisfied`, `cubic_r1cs`, `cubic_witness` in `src/r1cs.py`. All tests green.
- Write L, R, O matrices for (b) and (c) from Day 1 in `solutions/week-05/more_r1cs.py` and test them with your `is_satisfied`.
- **Deliverable:** green tests + extra R1CS

## Day 3 — Encrypting the witness
- Read *Building a ZK proof from an R1CS*.
- Implement the article's scheme with py_ecc: the prover sends `w` as G1 and G2 points; the verifier checks each row with pairings. Make it accept a valid witness and reject a wrong one.
- **Deliverable:** `solutions/week-05/encrypted_r1cs.py`

## Day 4 — Why this isn't good enough
- Watch the Daira Hopwood talk.
- List the problems with Day 3: proof size grows with the witness, the verifier work grows with the constraints, and the prover can send G1 and G2 points that don't encode the same value. Demonstrate the last one: make the verifier accept with inconsistent G1/G2 values.
- **Deliverable:** `solutions/week-05/day4.md` + attack script

## Day 5 — Underconstrained R1CS
- Take `out = x³ + x + 5` and delete one constraint. Find two different witnesses that give the same public `out`, or a witness with a wrong `out` that still passes.
- Write a helper that brute-forces all witnesses over F_97 for a given public output and reports whether the private part is unique. Run it on your Day 1 systems.
- **Deliverable:** `solutions/week-05/uniqueness.py`

## Day 6 — Exam (120 min, closed notes)
1. **Theory (30):** Explain why every constraint must be of the form `(linear) × (linear) = (linear)`, and why additions are "free" but multiplications cost a constraint.
2. **Coding (50):** Write the R1CS for `out = x⁴ − 2xy + y²` with the fewest constraints, plus a witness generator and 3 valid / 2 invalid tests.
3. **Debugging (20):** Given an R1CS for "`b` is a bit and `out = b·x`" that is missing the bit constraint, show a fake witness and fix it.

## Day 7 — Rest or catch up

## Exit criteria
- [ ] `tests.test_r1cs` green
- [ ] Can flatten an expression and write L, R, O by hand
- [ ] Can explain the G1/G2 consistency problem in "encrypted R1CS"
- [ ] Exam score in `progress.csv`
