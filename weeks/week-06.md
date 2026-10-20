# Week 6 — Polynomials, Lagrange interpolation and Schwartz–Zippel

**Goal:** the polynomial toolkit SNARKs run on: arithmetic, division with remainder, interpolation, vanishing polynomials, and the lemma that lets one random evaluation stand in for checking a whole polynomial.

**Reading:** [Lagrange interpolation](https://rareskills.io/post/python-lagrange-interpolation) · [Schwartz–Zippel lemma](https://rareskills.io/post/schwartz-zippel-lemma)
**Video:** [Multivariate polynomials and the Schwartz–Zippel lemma — Ryan O'Donnell](https://www.youtube.com/watch?v=Rzmj5OA-QqU) (Day 4)
**Code:** `src/poly.py` → `python3 -m unittest tests.test_poly -v`

## Day 1 — Polynomial arithmetic
- Implement `padd`, `psub`, `pmul`, `peval` (Horner) in `src/poly.py`. Note the representation: lowest degree first, no trailing zeros, `[]` is zero.
- **Deliverable:** add/mul/eval tests pass

## Day 2 — Division with remainder
- Implement `pdivmod` and `vanishing`.
- Prove on paper: `f(a) = 0` iff `(x − a)` divides `f`. Then: `f` vanishes on all of {x₁…xₙ} iff `t(x) = ∏(x − xᵢ)` divides `f`. This is the core trick of QAP.
- **Deliverable:** divmod and vanishing tests pass + `solutions/week-06/divisibility.md`

## Day 3 — Lagrange interpolation
- Read *Lagrange interpolation*.
- Implement `interpolate`. All of `tests.test_poly` green.
- Show uniqueness: two degree-< n polynomials that agree on n points are equal. Use your code to interpolate n points, then n+1 points, and look at the degree.
- **Deliverable:** green tests

## Day 4 — Schwartz–Zippel
- Read *Schwartz–Zippel*; watch the O'Donnell lecture.
- Experiment: take two different degree-d polynomials over F_97 and over F_(2^61−1). Evaluate at random points and measure how often they collide. Compare against the bound d / |F|.
- **Deliverable:** `solutions/week-06/sz_experiment.py` with a results table

## Day 5 — Putting it together
- Write a toy protocol: the prover claims `f(x) · g(x) = h(x)` for polynomials of degree ~1000 over BN254's scalar field. The verifier picks a random τ and checks one equation. Estimate the cheating probability.
- Explain in 5 lines why that random point must be unknown to the prover in advance (it's why trusted setups exist).
- **Deliverable:** `solutions/week-06/one_point_check.py` + notes

## Day 6 — Exam (120 min, closed notes)
1. **Theory (30):** State Schwartz–Zippel for one variable and prove it from "a non-zero degree-d polynomial has at most d roots".
2. **Coding (50):** From scratch, implement Lagrange interpolation and polynomial long division over F_p. Interpolate 5 points, divide by the vanishing polynomial of 3 of them, and check the remainder is zero only when it should be.
3. **Debugging (20):** An interpolation function works on small inputs but returns wrong polynomials or crashes when x values are negative or ≥ p. The bug: it computes `xi − xj` without reducing mod p and treats `x` and `x + p` as different points. Find inputs that break it and fix it.

## Day 7 — Rest or catch up

## Exit criteria
- [ ] `tests.test_poly` green
- [ ] Can explain why "t divides f" means "f vanishes on the domain"
- [ ] Can explain why one random evaluation is enough, and when it isn't
- [ ] Exam score in `progress.csv`
