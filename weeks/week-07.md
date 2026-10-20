# Week 7 — Quadratic Arithmetic Programs

**Goal:** convert an R1CS into a QAP and understand why "the witness satisfies every constraint" becomes "one polynomial divides another". After this week the whole SNARK pipeline up to the cryptography is yours.

**Reading:** [Quadratic Arithmetic Programs](https://rareskills.io/post/quadratic-arithmetic-program) · [R1CS to QAP over a finite field](https://rareskills.io/post/r1cs-to-qap)
**Video:** [Building a SNARK, pt 1 — Dan Boneh](https://www.youtube.com/watch?v=J4pVTamUBvU) (Day 5)
**Code:** `src/qap.py` (uses your `src/r1cs.py` and `src/poly.py`) → `python3 -m unittest tests.test_qap -v`

## Day 1 — The idea
- Read *Quadratic Arithmetic Programs*.
- Without code: for a 2-row R1CS, explain how each column of L becomes one polynomial, why the combined polynomial `u(x) = Σ wᵢ·Uᵢ(x)` equals row i of `L·w` at x = i, and why that turns n checks into one polynomial identity.
- **Deliverable:** `solutions/week-07/idea.md`

## Day 2 — R1CS → QAP
- Read *R1CS to QAP over a finite field*.
- Implement `r1cs_to_qap` and `combine` in `src/qap.py`.
- **Deliverable:** `test_columns_interpolate_matrix` and `test_t_vanishes_on_domain` pass

## Day 3 — The quotient polynomial
- Implement `quotient`. All of `tests.test_qap` green.
- Work out the degrees of u, v, w, t and h for an n-constraint system. Why is deg h = n − 2?
- **Deliverable:** green tests + degree table in `solutions/week-07/degrees.md`

## Day 4 — A bigger circuit
- Convert your Week 5 R1CS for `out = 3x²y + 5xy − x − 2y + 3` to a QAP. Check divisibility for 5 valid witnesses and show it fails for 5 corrupted ones (corrupt a different slot each time).
- **Deliverable:** `solutions/week-07/bigger_qap.py`

## Day 5 — Where QAP fits
- Watch the Boneh video. Map his "polynomial IOP + commitment" picture onto what you built: which part is the IOP, and what's still missing (hiding the witness, preventing the prover from choosing h after seeing τ).
- Re-run the Schwartz–Zippel spot check from the tests with τ chosen *after* the prover fixes h, and then with τ known in advance. Show how a prover who knows τ can cheat.
- **Deliverable:** `solutions/week-07/day5.md` + cheating script

## Day 6 — Exam (120 min, closed notes)
1. **Theory (30):** Prove: the witness satisfies the R1CS if and only if `t(x)` divides `u(x)v(x) − w(x)`.
2. **Coding (50):** From scratch, take a new 3-constraint R1CS (your choice), convert it to a QAP, compute h for a valid witness, and test that an invalid one leaves a remainder.
3. **Debugging (20):** A QAP converter interpolates rows instead of columns. Show a test it fails, explain why the result is meaningless, and fix it.

## Day 7 — Rest or catch up

## Exit criteria
- [ ] `tests.test_qap` green
- [ ] Can explain the R1CS ⇔ QAP equivalence and the degree of each polynomial
- [ ] Can show why τ must be unknown to the prover
- [ ] Exam score in `progress.csv`
