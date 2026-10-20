# Week 12 — On-chain Groth16 verification with Foundry

**Goal:** take a snarkjs-generated verifier, understand every line, and test it the way you'd test production settlement code: fuzzing, boundary values, malleability and replay.

**Reading:** [EIP-196](https://eips.ethereum.org/EIPS/eip-196) · [EIP-197](https://eips.ethereum.org/EIPS/eip-197) · re-read the EVM section of [Bilinear pairings](https://rareskills.io/post/bilinear-pairing) and the verifier part of [Groth16](https://rareskills.io/post/groth16)
**Video:** [Circom + SnarkJS full tutorial (2025)](https://www.youtube.com/watch?v=NG2NX1cDGUs) (Day 1; the verifier-export part) · optional: [BattleZips — Solidity verifiers](https://www.youtube.com/watch?v=zXHLIvIDO7w)

## Day 1 — Export and call the verifier
- Use your Week 10 `Polynomial(3)` circuit. Export the verifier with `snarkjs zkey export solidityverifier` and the calldata with `snarkjs zkey export soliditycalldata`.
- Set up `solutions/week-12/` as a Foundry project and write a test that verifies a real proof.
- **Deliverable:** one passing Foundry test

## Day 2 — Read every line
- Annotate the generated contract: where the verifying key lives, how the public-input linear combination is computed with 0x06/0x07, how the 4 pairings are packed for 0x08, and how G2 coordinates are ordered.
- Map each line to the Groth16 equation you implemented in Week 9.
- **Deliverable:** annotated copy `solutions/week-12/Verifier.annotated.sol`

## Day 3 — Negative tests and fuzzing
- Tests that must fail: a flipped bit in A, B or C; a wrong public input; a public input ≥ the scalar field r; a point not on the curve.
- Check whether the generated verifier rejects public inputs ≥ r. If it does, find the check; if your version doesn't, explain the attack (two different inputs, same field element).
- Fuzz the public inputs: any change must make a valid proof fail.
- **Deliverable:** negative tests + fuzz test

## Day 4 — Malleability on-chain
- Take a valid proof and produce `(−A, −B, C)` (negate the y-coordinates; for B, both Fp2 components). Show the verifier accepts it.
- Write a toy contract that wrongly uses `keccak256(proof)` as a replay guard and exploit it in a test. Fix it by using a nullifier that is a **public signal** of the circuit.
- **Deliverable:** exploit test + fixed contract

## Day 5 — Application-layer binding and gas
- A valid proof says nothing about *who* submits it or *when*. Add `msg.sender`-binding (or a recipient public signal), a chain ID, and a nonce or nullifier to your toy app, and write a test for each attack they stop.
- Measure gas for verification with 1, 3 and 6 public inputs and explain the slope.
- **Deliverable:** `solutions/week-12/app/` + gas table

## Day 6 — Exam (120 min, closed notes)
1. **Theory (30):** Explain why Groth16 proofs are malleable, why that's harmless for the proof system but dangerous for applications, and the correct way to build replay protection.
2. **Coding (50):** Given a fresh circuit, generate the verifier and write 3 valid and 3 invalid Foundry tests with reproducible commands.
3. **Debugging (20):** A contract checks the proof and then pays `msg.sender`, but the recipient is not a public signal. Write the front-running attack as a Foundry test and fix it.

## Day 7 — Rest or catch up

## Exit criteria
- [ ] Can explain every line of the generated verifier
- [ ] Malleability and replay exploited and fixed in tests
- [ ] Field-range behaviour of public inputs tested
- [ ] Exam score in `progress.csv`
