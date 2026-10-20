# Week 3 — Elliptic curves

**Goal:** implement elliptic-curve arithmetic from scratch, then use BN254 (the curve Ethereum's precompiles use) through `py_ecc`. Understand subgroups and cofactors, because invalid-point bugs are real.

**Reading:** [Elliptic curve addition](https://rareskills.io/post/elliptic-curve-addition) · [Elliptic curves over finite fields](https://rareskills.io/post/elliptic-curves-finite-fields)
**Video:** [Lectures on ECC — Alfred Menezes](https://www.youtube.com/watch?v=LdYtsMyPnyc) (Day 1). Reference when stuck: [PSE ECC course playlist](https://www.youtube.com/playlist?list=PLV91V4b0yVqQ_inAjuIB5SwBNyYmA9S6M)
**Code:** `src/ec.py` → `python3 -m unittest tests.test_ec -v` · `pip install -r requirements.txt` for `py_ecc`

## Day 1 — The group law over the reals
- Read *Elliptic curve addition*; watch the Menezes lecture.
- Derive the chord-and-tangent formulas yourself: the slope for P + Q and for doubling, then x₃ and y₃.
- **Deliverable:** `solutions/week-03/derivation.md`

## Day 2 — Curves over F_p
- Read *Elliptic curves over finite fields*.
- Implement `is_on_curve`, `neg`, `add` in `src/ec.py` for y² = x³ + 3 over F_101. Handle INF, P + (−P), and doubling a point with y = 0.
- **Deliverable:** identity / inverse / closure tests pass

## Day 3 — Scalar multiplication and group order
- Implement `scalar_mul` (double-and-add) and `all_points`. All of `tests.test_ec` green.
- The curve has 102 points = 2 · 3 · 17. Find a generator of the order-17 subgroup by multiplying random points by the cofactor 6. This is the same pattern as BN254's G2 cofactor.
- **Deliverable:** green tests + `solutions/week-03/subgroups.py`

## Day 4 — BN254 with py_ecc
- Using `py_ecc.bn128`: check that `G1` is on the curve, `multiply(G1, curve_order)` is the point at infinity, and `add(multiply(G1, a), multiply(G1, b)) == multiply(G1, a + b)`.
- Re-do Week 2's "verify a sum without seeing the numbers", now with `a·G1` instead of `5^a`. Then verify a linear equation `3a + 5b = c` from `[a]G`, `[b]G`, `[c]G`.
- **Deliverable:** `solutions/week-03/bn254.py`

## Day 5 — When points go wrong
- Pass a point that is not on your curve into your `add` before the `ValueError` check existed (comment it out). What does the formula return? Research "invalid curve attack" and write 5 lines on why on-chain verifiers must check inputs.
- Note: field elements are reduced mod the **base field** p; scalars are reduced mod the **group order** r. For BN254 these are different 254-bit primes. Write down both numbers and what goes wrong if you mix them up.
- **Deliverable:** `solutions/week-03/day5.md`

## Day 6 — Exam (120 min, closed notes)
1. **Theory (30):** Derive the doubling formula. Explain why the group order of any point divides the number of points on the curve.
2. **Coding (50):** Implement point addition and double-and-add for y² = x³ + 7 over F_107 from scratch (no copying). Write 5 tests including P + (−P) and scalar = group order.
3. **Debugging (20):** This `add` passes most tests but fails some: `if p1 == p2: lam = (3*x1*x1) * inv(2*y1)` with no other special cases. Find every input that breaks it and fix it.

## Day 7 — Rest or catch up

## Exit criteria
- [ ] `tests.test_ec` green
- [ ] Can do one point addition by hand over a small field
- [ ] Know the difference between BN254's base field p and scalar field r
- [ ] Exam score in `progress.csv`
