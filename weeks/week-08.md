# Week 8 — Trusted setup and evaluating a QAP on it

**Goal:** evaluate polynomials at a secret point τ that nobody knows, using powers of τ hidden in elliptic-curve points. Build the naive SNARK, then break it — that's the motivation for Groth16.

**Reading:** [Trusted setup](https://rareskills.io/post/trusted-setup) · [Evaluating a QAP on a trusted setup](https://rareskills.io/post/elliptic-curve-qap)
**Video:** [Powers of Tau — Solidity Fridays](https://www.youtube.com/watch?v=TcQXzGTSXfo) (Day 5)

## Day 1 — Powers of tau
- Read *Trusted setup*.
- In Python with py_ecc: generate `[τ⁰]G1 … [τᵈ]G1` and `[τ⁰]G2 … [τᵈ]G2`. Write `eval_hidden(f, srs)` that returns `[f(τ)]G1` from the coefficients of f and the SRS alone, then check it against `multiply(G1, f(τ))`.
- **Deliverable:** `solutions/week-08/srs.py` with tests

## Day 2 — Checking a product in the exponent
- Using your SRS, the prover sends `[f(τ)]G1`, `[g(τ)]G2`, `[h(τ)]G1`. The verifier checks `f(τ)·g(τ) = h(τ)` with one pairing equation. Test valid and invalid triples.
- **Deliverable:** `solutions/week-08/product_check.py`

## Day 3 — The naive QAP SNARK
- Read *Evaluating a QAP on a trusted setup*.
- Plug in your Week 7 QAP: the setup also publishes `[t(τ)·τⁱ]G1`, the prover computes `[A]1 = [u(τ)]1`, `[B]2 = [v(τ)]2`, `[C]1 = [w(τ) + h(τ)t(τ)]1`, and the verifier checks `e(A, B) = e(C, G2)`.
- **Deliverable:** end-to-end prove + verify for the cubic circuit

## Day 4 — Break it
- Forge a proof without a witness: pick any `A`, `B` and set `C` so the equation holds. Then forge one where `A` is not even a combination of the circuit's U polynomials.
- Write a list of everything the verifier fails to enforce (A, B, C come from the circuit; the same witness is used in all three; public inputs are bound). Groth16 fixes each item — keep the list for Week 9.
- **Deliverable:** `solutions/week-08/forgery.py` + `solutions/week-08/what_is_missing.md`

## Day 5 — Ceremonies
- Watch the Powers of Tau video.
- Simulate a 3-party ceremony: each participant multiplies the previous SRS by their own secret. Show that the final τ is the product of all secrets, and that one honest participant who deletes their secret is enough.
- How would a participant prove they used the same secret across all powers? Sketch the pairing check.
- **Deliverable:** `solutions/week-08/ceremony.py`

## Day 6 — Exam (120 min, closed notes)
1. **Theory (30):** Explain what "toxic waste" is and show concretely how knowing τ lets someone forge a proof for the naive scheme.
2. **Coding (50):** From scratch, build an SRS of degree 4 and evaluate a hidden polynomial; then implement the verifier's pairing check for `f(τ)g(τ) = h(τ)` with 2 valid and 2 invalid tests.
3. **Debugging (20):** A ceremony implementation updates `[τⁱ]G1` with the new secret but forgets to update `[τⁱ]G2`. Show the check that catches it and what an attacker could do if nobody checks.

## Day 7 — Rest or catch up

## Exit criteria
- [ ] Naive QAP SNARK works end to end
- [ ] Can forge a naive proof and explain why
- [ ] Can explain why one honest ceremony participant is enough
- [ ] Exam score in `progress.csv`
