# Week 4 — Bilinear pairings (Python and EVM)

**Goal:** understand what a pairing gives you — one multiplication between hidden values — and call the EVM's pairing precompile yourself. This is the week your Solidity skills start paying off.

**Reading:** [Bilinear pairings in Python, Solidity and the EVM](https://rareskills.io/post/bilinear-pairing) · [EIP-196](https://eips.ethereum.org/EIPS/eip-196) · [EIP-197](https://eips.ethereum.org/EIPS/eip-197)
**Video:** [Elliptic Curve Pairings — Demystifying Cryptography Fundamentals (3/3)](https://www.youtube.com/watch?v=FE70-F_wkGw) (Day 1)

## Day 1 — What a pairing is
- Read the first half of *Bilinear pairings*; watch the video.
- Write down: G1, G2, GT, which field each lives over, and the bilinearity rule `e(aP, bQ) = e(P, Q)^(ab)`. Explain why G1 and G2 are different groups on BN254.
- **Deliverable:** `solutions/week-04/notes.md`

## Day 2 — Pairings in py_ecc
- With `py_ecc.bn128.pairing`, check bilinearity for 3 random (a, b).
- Prove you know a, b with `a · b = c` given only `[a]G1`, `[b]G2`, `[c]G1`: check `e([b]G2, [a]G1) == e(G2, [c]G1)`.
- Then extend Week 3's linear check to a quadratic one: verify `a·b + 3c = d` from hidden values.
- **Deliverable:** `solutions/week-04/pairings.py`

## Day 3 — The EVM precompiles
- Finish *Bilinear pairings* (EVM part) and read EIP-196/197.
- Create `solutions/week-04/evm/` as a Foundry project. Write a test that calls `ecAdd` (0x06) and `ecMul` (0x07) and checks the result against values you computed in Python.
- **Deliverable:** Foundry tests passing for ecAdd and ecMul

## Day 4 — Calling ecPairing (0x08)
- Write a Solidity function that takes `[a]G1`, `[b]G2`, `[c]G1` and returns true iff `ab = c`, using one call to 0x08. The precompile checks that a product of pairings equals 1, so you'll need to negate one G1 point.
- Watch out: EIP-197 encodes G2 coordinates with the imaginary part first. Get it wrong once on purpose and record what happens.
- **Deliverable:** passing valid-case test and failing invalid-case test

## Day 5 — Costs and attack surface
- Measure the gas of your pairing check for 2 and 4 pairs. Work out the per-pair cost from EIP-1108's numbers.
- What does 0x08 do with a G1 point that is not on the curve? With a G2 point not in the right subgroup? Test both and write down what your verifier can and can't assume.
- **Deliverable:** `solutions/week-04/day5.md` with gas table and findings

## Day 6 — Exam (120 min, closed notes)
1. **Theory (30):** Using bilinearity, prove that `e(aP, bQ) = e(abP, Q)`. Explain why pairings give you exactly one multiplication between hidden values, not two.
2. **Coding (50):** From a blank file, write a Python check (py_ecc) and a Solidity check (0x08) for "`a · b = c + d`" from `[a]G1`, `[b]G2`, `[c]G1`, `[d]G1`. One valid and two invalid test cases for each.
3. **Debugging (20):** A verifier returns true for every input. The bug: it ignores the return-data of the staticcall and only checks the success flag. Explain why that's wrong and fix it.

## Day 7 — Rest or catch up

## Exit criteria
- [ ] Bilinearity checked in Python and on-chain
- [ ] Can explain the G2 encoding order in EIP-197
- [ ] Exam score in `progress.csv`
