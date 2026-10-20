# Week 9 — Groth16

**Goal:** implement Groth16 setup, prover and verifier yourself, and know what every element is for. This is the core week of the course; give it full attention.

**Reading:** [Groth16 explained](https://rareskills.io/post/groth16) · written companion: [zkSecurity — How Groth16 works](https://blog.zksecurity.xyz/posts/pudding-10-groth16/)
**Video:** [How Groth16 Works — David Wong](https://www.youtube.com/watch?v=8Tl20_XUZLI) (~1 h, split over Days 1 and 3). Optional second view: [DoraHacks — Groth16](https://www.youtube.com/watch?v=VQyDSxB9Bls)
**Code:** `solutions/week-09/groth16.py`, built on your `src/qap.py` and py_ecc

## Day 1 — α and β: stopping the forgery
- Read *Groth16* up to the introduction of α and β; watch the first half of the video.
- Take your Week 8 forgery list. Show how adding `[α]1`, `[β]2` to the setup and `e(A, B) = e(α, β) · e(C, G2)` blocks the Day-4 forgery. Implement this intermediate scheme.
- **Deliverable:** intermediate scheme + forgery now fails

## Day 2 — Public inputs: γ and δ
- Continue *Groth16*: splitting the witness into public and private parts, and the γ and δ separation.
- Implement the full setup: for each witness column compute `βUᵢ(τ) + αVᵢ(τ) + Wᵢ(τ)`, divided by γ for public slots and δ for private ones; plus `[τⁱ t(τ)/δ]1`.
- **Deliverable:** `setup(qap, n_public)` returning proving and verifying keys

## Day 3 — The prover with blinding
- Finish the article and the video.
- Implement `prove`: compute A, B, C with random r and s. Check that two proofs of the same witness look unrelated.
- **Deliverable:** `prove(pk, witness)`

## Day 4 — The verifier
- Implement `verify(vk, public_inputs, proof)` with the 4-pairing equation `e(A, B) = e(α, β) · e(Σ pubᵢ·Kᵢ, γ) · e(C, δ)`.
- Tests: valid proof passes; changing any public input fails; using a proof for a different statement fails; a forged proof from Week 8 fails.
- **Deliverable:** full end-to-end Groth16 for the cubic circuit, with tests

## Day 5 — Malleability
- Show that `(−A, −B, C)` is also a valid proof, and that `(A·k⁻¹, B·k, C)` is valid for any non-zero k. Take a valid proof, transform it, and confirm `verify` accepts it.
- Write down what this means for applications: **a proof is not a unique identifier**. Never use proof bytes as a nullifier or replay key. You'll test this on-chain in Week 12.
- **Deliverable:** `solutions/week-09/malleability.py` + notes

## Day 6 — Exam (120 min, closed notes)
1. **Theory (30):** Write the Groth16 verification equation and explain the purpose of α, β, γ, δ, r, s. What breaks if δ is removed?
2. **Coding (50):** Without looking at your solution, implement `verify` and write the 4 tests from Day 4.
3. **Debugging (20):** A setup uses δ for both public and private slots (no γ). Show how a prover can change a public input and still produce an accepting proof, or explain precisely why the separation matters.

## Day 7 — Rest or catch up

## Exit criteria
- [ ] Working Groth16 in Python with your own setup, prover and verifier
- [ ] Can write the verification equation from memory and explain every term
- [ ] Can demonstrate proof malleability
- [ ] Exam score in `progress.csv`
