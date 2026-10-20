# Week 2 — Sets, groups and homomorphisms

**Goal:** know exactly what a group is, why element orders divide the group order, and why "computing on hidden values" works (homomorphisms). Elliptic curves and Groth16 are built on these ideas.

**Reading:** [Set theory](https://rareskills.io/post/set-theory) · [Abstract algebra](https://rareskills.io/post/abstract-algebra) · [Group theory](https://rareskills.io/post/group-theory) · [Homomorphisms](https://rareskills.io/post/homomorphisms)
**Video:** [Group Theory — Demystifying Cryptography Fundamentals (1/3)](https://www.youtube.com/watch?v=3N059G8H6b0) (Day 3)
**Code:** `src/algebra.py` → `python3 -m unittest tests.test_algebra -v`

## Day 1 — Sets and algebraic structures
- Read *Set theory* and *Abstract algebra*. Make a one-page table: magma, semigroup, monoid, group, abelian group — what each one adds, plus one example and one non-example each.
- **Deliverable:** `solutions/week-02/structures.md`

## Day 2 — Groups in code
- Read the first half of *Group theory*.
- Implement `is_group` in `src/algebra.py` by brute force. Check: (Z_n, +), (Z_p*, ×), and why including 0 in the multiplicative set breaks it.
- **Deliverable:** the `is_group` tests pass

## Day 3 — Orders and cyclic subgroups
- Finish *Group theory*; watch the koalateectrl video.
- Implement `order_of`, `is_generator`, `subgroup`. All of `tests.test_algebra` green.
- Print the order of every element of F_97*. Check that every order divides 96 (Lagrange's theorem) and count how many generators there are. Compare with φ(96).
- **Deliverable:** green tests + `solutions/week-02/orders.txt`

## Day 4 — Homomorphisms
- Read *Homomorphisms*.
- Show in code that `f(x) = 5^x mod 97` is a homomorphism from (Z_96, +) to (F_97*, ×): `f(a+b) = f(a)·f(b)` for all a, b.
- Use it to "verify a sum without seeing the numbers": given `f(a)`, `f(b)`, `f(c)`, check that `a + b = c` (mod 96) without knowing a, b, c.
- **Deliverable:** `solutions/week-02/homomorphism.py`

## Day 5 — Limits of hiding
- Extend Day 4: can you check `a · b = c` from `f(a)`, `f(b)`, `f(c)` alone? Write why not. (This gap is exactly what pairings fix in Week 4.)
- Why is the hiding weak with p = 97? Brute-force the discrete log of `5^x` for a random x. Note how many steps it took and what changes with a 254-bit group.
- **Deliverable:** `solutions/week-02/day5.md`

## Day 6 — Exam (120 min, closed notes)
1. **Theory (30):** State and prove Lagrange's theorem for finite groups (cosets). Deduce that `g^(p-1) = 1` in F_p*.
2. **Coding (50):** Without looking at your solution, implement `order_of` and find all generators of F_101*. Then implement `discrete_log(g, h, p)` by brute force and test it on 3 inputs.
3. **Debugging (20):** A teammate claims (Z_10, ×) restricted to {1, 3, 7, 9} is not a group "because 3·3 = 9 and 9·9 = 1 is weird". Decide who's right, prove it, and give the inverse of each element.

## Day 7 — Rest or catch up

## Exit criteria
- [ ] `tests.test_algebra` green
- [ ] Can explain why element order divides group order
- [ ] Can explain what a homomorphism lets a verifier check, and what it doesn't
- [ ] Exam score in `progress.csv`
