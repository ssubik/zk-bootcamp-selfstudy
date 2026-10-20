# Week 1 — Arithmetic circuits and finite fields

**Goal:** think of a computation as a set of equations over a prime field, and be fluent in modular arithmetic, especially inverses.

**Reading:** [P vs NP](https://rareskills.io/post/p-vs-np) · [Arithmetic circuits](https://rareskills.io/post/arithmetic-circuit) · [Finite fields](https://rareskills.io/post/finite-fields)
**Video:** [What is a SNARK? — Dan Boneh](https://www.youtube.com/watch?v=h-94UhJLeck) (Day 1) · [Paar Lecture 11: Euclidean algorithm & Euler's theorem](https://www.youtube.com/watch?v=fq6SXByItUI) (Day 3)
**Code:** `src/field.py` → `python3 -m unittest tests.test_field -v`

## Day 1 — Why circuits?
- Read *P vs NP* and watch the Boneh video. Write half a page: what a prover and verifier are, and why "checking is easier than solving" is the whole point.
- Read the first half of *Arithmetic circuits*. By hand, write constraint systems for: (a) `x` is 0 or 1; (b) `z = x AND y` for bits; (c) `x` is one of {2, 3, 7}.
- **Deliverable:** `solutions/week-01/day1.md`

## Day 2 — Circuits as equations
- Finish *Arithmetic circuits*. Note how the article proves graph colouring or similar NP problems with constraints.
- Write a Python function `check(constraints, assignment)` where each constraint is a lambda returning `True`/`False`. Encode your Day 1 circuits plus "`x` is a 4-bit number" (bits + recomposition) and test valid and invalid assignments.
- **Deliverable:** `solutions/week-01/circuits.py` with ≥ 6 tests

## Day 3 — Finite fields
- Read *Finite fields* and watch Paar Lecture 11.
- Implement `add`, `sub`, `neg`, `mul`, `inv` (Fermat) in `src/field.py`. Make them normalise negative inputs.
- **Deliverable:** the first half of `tests.test_field` passes

## Day 4 — Two ways to invert
- Implement `inv_euclid` (extended Euclid, no `pow`) and `div`. All of `tests.test_field` must pass.
- On paper: show why `a^(p-2)` is the inverse, and why 0 has none. Compute `inv(17)` mod 97 by hand with extended Euclid.
- **Deliverable:** green tests; derivation in `solutions/week-01/day4.md`

## Day 5 — Fields meet circuits
- Redo Day 2's `check` over F_97. First drop the recomposition constraint and show `x` can then be anything. Then try "`x` is a 7-bit number": since 2⁷ = 128 > 97, find two different bit patterns that recompose to the same field element. Write down what this tells you about overflow and aliasing in ZK (you'll meet it again as `Num2Bits_strict` in Week 11).
- Why is "`x ≠ 0`" hard to express as an equation? Show the trick: introduce `inv` as a witness and constrain `x · inv = 1`. You'll see this again as `IsZero` in Circom.
- **Deliverable:** `solutions/week-01/day5.md`

## Day 6 — Exam (120 min, closed notes)
1. **Theory (30):** Prove that every non-zero element of F_p has a unique inverse. Explain why F_p needs p prime (show the failure for mod 12).
2. **Coding (50):** In a fresh file, implement a `Fp` class with `+ - * /`, `==` and `**`, for any prime. Write 5 tests including negative inputs and division by zero.
3. **Debugging (20):** This circuit claims "`b` is a bit and `y = b ? x : 0`": `b*(b-1) = 0`, `y = b + x`. Find the bug, give a satisfying wrong assignment, and fix it.

## Day 7 — Rest or catch up

## Exit criteria
- [ ] `tests.test_field` green
- [ ] Can compute a modular inverse by hand
- [ ] Can write constraints for bit checks, set membership and `x ≠ 0`
- [ ] Exam score in `progress.csv`
