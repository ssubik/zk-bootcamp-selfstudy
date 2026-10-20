# Week 16 (optional) — KZG polynomial commitments

**Goal:** commit to a polynomial with one curve point and open it at any point with one more — the commitment scheme inside PLONK and Ethereum's EIP-4844 blobs. You already have every piece from Weeks 6, 8 and 9.

**Videos:** [ZKP MOOC Lecture 6: Polynomial commitments based on pairing and discrete log — Yupeng Zhang](https://www.youtube.com/watch?v=WyT5KkKBJUw) (Day 1) · [KZG Commitments — Ben Edgington](https://www.youtube.com/watch?v=g6s4zpypPT4) (Day 4)

## Day 1 — The scheme
- Watch Lecture 6 (KZG part). Write down commit, open and verify, and the identity `f(x) − f(z) = q(x)·(x − z)`.

## Day 2 — Implement it
- Reusing your Week 8 SRS and Week 6 `pdivmod`: implement `commit(f)`, `open(f, z) → (f(z), [q(τ)]1)`, and `verify(C, z, y, π)` with one pairing equation.
- **Deliverable:** `solutions/week-16/kzg.py` with tests

## Day 3 — Break it
- Show that a wrong `y` fails, and that someone who knows τ can open a commitment to any value. Implement batch opening at two points.

## Day 4 — KZG on Ethereum
- Watch the Ben Edgington talk. Read about the point-evaluation precompile introduced with EIP-4844 and write a Foundry test that calls it with a valid input.

## Day 5 — Connect back
- Write one page: where KZG appears inside PLONK, why Groth16 doesn't need a separate commitment scheme, and what FRI-based (STARK) systems use instead.

## Day 6 — Exam (120 min)
1. **Theory (30):** Prove KZG opening correctness and explain why binding depends on τ staying secret.
2. **Coding (50):** Implement commit/open/verify from scratch with 3 tests.
3. **Debugging (20):** A verifier checks `e(C − [y]1, G2) = e(π, [τ]2)`, forgetting to subtract `[z]2`. Show that it accepts `y = f(0)` as the opening at *any* z, and fix it.

## Day 7 — Rest

## Where to go next
Pick one: Noir (PLONK-based, Rust-like syntax), halo2 (recursion, no trusted setup), or a STARK stack. Your capstone statement is a good first program to port.
