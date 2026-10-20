# Week 11 — Circom security: underconstrained circuits

**Goal:** the most common real ZK bug is a circuit that accepts witnesses it shouldn't. This week you learn to write, find and exploit those bugs — the same invariant mindset you use in Foundry, applied to constraints.

**Reading:** [Components in a loop](https://rareskills.io/post/circom-component-loop) · [Conditional statements](https://rareskills.io/post/circom-if-statement) · [Quin selector](https://rareskills.io/post/quin-selector) · [Hacking underconstrained circuits with fake proofs](https://rareskills.io/post/underconstrained-circom) · [AliasCheck and Num2Bits_strict](https://rareskills.io/post/circom-aliascheck) · [ZK-friendly hash functions](https://rareskills.io/post/zk-friendly-hash) · [Tornado Cash line by line](https://rareskills.io/post/how-does-tornado-cash-work) · zkSecurity: [Circom pitfalls Part 1](https://blog.zksecurity.xyz/posts/circom-pitfalls-1/) and [Part 2](https://blog.zksecurity.xyz/posts/circom-pitfalls-2/)
**Video:** [Picus: push-button ZK circuit verification — Shankara Pailoor](https://www.youtube.com/watch?v=4iDhdEmwnlQ) (Day 3) · [Tornado Cash — How it Works](https://www.youtube.com/watch?v=z_cRicXX1jI) (Day 5)

## Day 1 — Loops, conditionals, selectors
- Read *Components in a loop*, *Conditional statements* and *Quin selector*.
- Build `Select(N)`: given a private array and a private index, output the element at that index. Make sure an out-of-range index cannot produce an output.
- **Deliverable:** circuit + tests including index = N

## Day 2 — Fake proofs
- Read *Hacking underconstrained circuits*.
- Reproduce the article's attack: take a circuit with a `<--` that isn't constrained, write a malicious witness by hand (edit the `.wtns` or skip the witness calculator), generate a proof, and get `snarkjs groth16 verify` to accept a false statement.
- **Deliverable:** `solutions/week-11/fake_proof/` with the circuit, the forged witness and the verify output

## Day 3 — The pitfall catalogue
- Read zkSecurity Parts 1 and 2; watch the Picus talk.
- For each pitfall (assert vs constraint, unconstrained hints, aliasing, unconstrained component outputs, unchecked component inputs, signed comparisons), write a 5-line vulnerable circuit and a fixed version.
- **Deliverable:** `solutions/week-11/pitfalls/` — one folder per pitfall

## Day 4 — Range checks and comparators
- Read *AliasCheck and Num2Bits_strict*.
- `LessThan(n)` from circomlib only works if both inputs fit in n bits. Show that `LessThan(8)` gives a wrong answer for an input of 300 when nothing range-checks it, and fix it with `Num2Bits`. Then show why `Num2Bits(254)` can alias and when you need `_strict`.
- **Deliverable:** `solutions/week-11/comparators/` + notes on which bit-widths you'll use in the capstone

## Day 5 — A real system: Tornado Cash
- Read *ZK-friendly hash functions* and *Tornado Cash line by line*; watch the video.
- Write down: what is public, what is private, what the nullifier prevents, and what binds the proof to the recipient address (why front-running a withdrawal doesn't work).
- **Deliverable:** `solutions/week-11/tornado.md` — this is the template for your capstone threat model

## Day 6 — Exam (120 min, closed notes)
1. **Theory (30):** Explain aliasing in `Num2Bits(254)` with BN254's scalar field, and why circomlib comparators need range-checked inputs.
2. **Coding (50):** You get a 30-line circuit with two planted bugs (have a friend or an AI write it without telling you where, or use one of RareSkills' puzzles). Find both, write a fake proof for one, and fix both.
3. **Debugging (20):** In a Tornado-style circuit, the recipient address is a public input but never used in any constraint. Explain the attack and the one-line fix.

## Day 7 — Rest or catch up

## Exit criteria
- [ ] Produced at least one accepted fake proof for an underconstrained circuit
- [ ] Have vulnerable + fixed examples for every pitfall
- [ ] Know exactly which range checks your capstone needs
- [ ] Exam score in `progress.csv`
