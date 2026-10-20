# Week 15 (optional) — PLONK

**Goal:** understand the proof system behind most modern stacks (Noir/Barretenberg, halo2-style systems, many zkEVMs): a universal setup, custom gates, and the permutation argument for wiring.

**Reading:** [Understanding PLONK — David Wong](https://cryptologie.net/article/527/understanding-plonk) · [The permutation argument (RareSkills)](https://rareskills.io/post/permutation-argument)
**Videos:** [Building a SNARK, pt 2 — Dan Boneh](https://www.youtube.com/watch?v=vxyoPM2m7Yg) (Day 1) · [ZKP MOOC Lecture 5: The Plonk SNARK — Dan Boneh](https://www.youtube.com/watch?v=A0oZVEXav24) (Days 3–4)

## Day 1 — PLONK's circuit model
- Watch Boneh pt 2. Write the PLONK gate equation `qL·a + qR·b + qO·c + qM·a·b + qC = 0` and express your Week 5 cubic circuit as a table of gates.
- **Deliverable:** `solutions/week-15/gates.md`

## Day 2 — Wiring and the permutation argument
- Read *The permutation argument*. Explain how copy constraints ("this gate's output is that gate's input") are enforced, and why R1CS didn't need this.
- **Deliverable:** notes + a small Python check that two vectors are permutations using the grand-product idea

## Day 3 — The protocol, round by round
- Read David Wong's article; watch the first half of Lecture 5. List each prover round and what the verifier learns.

## Day 4 — Compare with Groth16
- Finish Lecture 5. Fill a table: setup type, proof size, verifier pairings, prover cost, custom gates. When would you choose each?
- **Deliverable:** `solutions/week-15/groth16_vs_plonk.md`

## Day 5 — Hands-on
- Rebuild your capstone statement with `snarkjs plonk setup` and compare proof size, proving time and verifier gas against your Groth16 version.

## Day 6 — Exam (120 min)
1. **Theory (30):** Explain the permutation argument and why PLONK's setup is universal.
2. **Coding (50):** Write the gate table and copy constraints for `out = (x + y)·z − 4`, and check it with a Python script.
3. **Debugging (20):** A gate table is satisfied gate by gate but the circuit proves the wrong statement. Find the missing copy constraint.

## Day 7 — Rest
