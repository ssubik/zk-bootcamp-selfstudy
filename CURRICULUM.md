# ZK Curriculum — overview and map

This is the single plan for the course. Each week's file in [`weeks/`](weeks/) has the day-by-day detail; this page is the map, the rules, and the verified resource list. Independent study plan built on the public [RareSkills ZK Book](https://rareskills.io/zk-book); not affiliated with RareSkills.

## What "proficient" means here

By the end of Week 14 you should be able to, without notes:

1. Take a small program, write its R1CS by hand, convert it to a QAP, and explain why a valid witness makes `U·V − W` divisible by `t`.
2. Implement Groth16 setup, prover and verifier in Python with `py_ecc`, and explain what each of α, β, γ, δ, r, s is for.
3. Write Circom circuits that are **fully constrained**, find underconstraint bugs in other people's circuits, and know the classic pitfalls (`<--` hints, aliasing, comparator bit-widths, `assert` vs `===`).
4. Ship an on-chain Groth16 verifier with Foundry tests covering malleability, field-range checks, public-input binding and replay.
5. Design a ZK application end to end: what is public, what is private, what binds the private data to reality, and what the threat model is.

Weeks 15–16 (optional) take you past Groth16 to PLONK and KZG, which is what most modern systems use.

## Schedule

5 study days + 1 exam day + 1 rest day per week. Target **2–2.5 hours** on a study day:

| Block | Time |
|---|---|
| Review yesterday's notes / redo one exercise from memory | 20 min |
| Reading (and the week's video on the day it is assigned) | 45 min |
| Coding / derivation | 60–75 min |
| Notes: 5 lines on what you learned, 1 line on what is still unclear | 10 min |

**Heavy work week?** Stretch the week over two calendar weeks rather than skipping the exam. Don't skip ahead; every phase uses the previous one.

| Phase | Weeks | Theme | Code you build |
|---|---|---|---|
| 1. Math foundations | 1–3 | Fields, groups, elliptic curves | `src/field.py`, `src/algebra.py`, `src/ec.py` |
| 2. SNARK pipeline | 4–9 | Pairings → R1CS → polynomials → QAP → trusted setup → Groth16 | `src/r1cs.py`, `src/poly.py`, `src/qap.py`, `solutions/week-09/groth16.py` |
| 3. Circom | 10–11 | Constraint design, then constraint security | Circom circuits + attack writeups |
| 4. On-chain + capstone | 12–14 | Solidity verifier, Foundry, capstone | `capstone/` |
| 5. Beyond Groth16 (optional) | 15–16 | PLONK, KZG | Toy KZG in Python |

| Week | Topic | Guide |
|---|---|---|
| 1 | Arithmetic circuits and finite fields | [week-01](weeks/week-01.md) |
| 2 | Sets, groups and homomorphisms | [week-02](weeks/week-02.md) |
| 3 | Elliptic curves | [week-03](weeks/week-03.md) |
| 4 | Bilinear pairings (Python and EVM) | [week-04](weeks/week-04.md) |
| 5 | R1CS and a first ZK proof from R1CS | [week-05](weeks/week-05.md) |
| 6 | Polynomials, Lagrange interpolation, Schwartz–Zippel | [week-06](weeks/week-06.md) |
| 7 | QAP | [week-07](weeks/week-07.md) |
| 8 | Trusted setup and evaluating a QAP on it | [week-08](weeks/week-08.md) |
| 9 | Groth16 | [week-09](weeks/week-09.md) |
| 10 | Circom fundamentals and design patterns | [week-10](weeks/week-10.md) |
| 11 | Circom security: underconstrained circuits | [week-11](weeks/week-11.md) |
| 12 | On-chain Groth16 verification with Foundry | [week-12](weeks/week-12.md) |
| 13 | Capstone: build | [week-13](weeks/week-13.md) |
| 14 | Capstone: harden, final exam, write-up | [week-14](weeks/week-14.md) |
| 15 | Optional: PLONK | [week-15](weeks/week-15.md) |
| 16 | Optional: KZG polynomial commitments | [week-16](weeks/week-16.md) |

## Day 6 exams

Each week has its own exam in its guide. All exams: **120 minutes, closed notes, 100 points** — 30 theory, 50 coding, 20 debugging. Pass 75, distinction 90. Grade against the week's exit criteria, be strict, and record the score in `progress.csv`. Below 75: redo the weakest day before moving on.

## Repository conventions

- Exercise stubs live in `src/`; tests in `tests/`. Run one week at a time, e.g. `python3 -m unittest tests.test_ec -v`. Future weeks' tests fail until you reach them; that is expected.
- Your own work goes under `solutions/week-NN/` (free-form: notes, scripts, Circom, Foundry projects).
- Log every study day in `progress.csv`.

## Verified resources

### Reading (all links checked against the RareSkills ZK Book table of contents, October 2026)

Module 1 — math: [P vs NP](https://rareskills.io/post/p-vs-np) · [Arithmetic circuits](https://rareskills.io/post/arithmetic-circuit) · [Finite fields](https://rareskills.io/post/finite-fields) · [Set theory](https://rareskills.io/post/set-theory) · [Abstract algebra](https://rareskills.io/post/abstract-algebra) · [Group theory](https://rareskills.io/post/group-theory) · [Homomorphisms](https://rareskills.io/post/homomorphisms) · [Elliptic curve addition](https://rareskills.io/post/elliptic-curve-addition) · [Elliptic curves over finite fields](https://rareskills.io/post/elliptic-curves-finite-fields)

Module 2 — Groth16: [Bilinear pairings](https://rareskills.io/post/bilinear-pairing) · [R1CS](https://rareskills.io/post/rank-1-constraint-system) · [ZK proof from R1CS](https://rareskills.io/post/r1cs-zkp) · [Lagrange interpolation](https://rareskills.io/post/python-lagrange-interpolation) · [Schwartz–Zippel](https://rareskills.io/post/schwartz-zippel-lemma) · [QAP](https://rareskills.io/post/quadratic-arithmetic-program) · [R1CS to QAP](https://rareskills.io/post/r1cs-to-qap) · [Trusted setup](https://rareskills.io/post/trusted-setup) · [QAP on a trusted setup](https://rareskills.io/post/elliptic-curve-qap) · [Groth16](https://rareskills.io/post/groth16)

Module 3 — Circom: [Intro](https://rareskills.io/post/circom-intro) · [Hello world](https://rareskills.io/post/hello-world-circom) · [Syntax](https://rareskills.io/post/circom-syntax) · [Quadratic constraints](https://rareskills.io/post/quadratic-constraints) · [Symbolic variables](https://rareskills.io/post/circom-symbolic-variable) · [Intermediate signals](https://rareskills.io/post/circom-intermediate-signals) · [Public/private inputs](https://rareskills.io/post/circom-public-private-inputs) · [Indicate then constrain](https://rareskills.io/post/indicate-then-constrain) · [Compute then constrain](https://rareskills.io/post/compute-then-constrain) · [Components in a loop](https://rareskills.io/post/circom-component-loop) · [Underconstrained circuits](https://rareskills.io/post/underconstrained-circom) · [AliasCheck / Num2Bits_strict](https://rareskills.io/post/circom-aliascheck) · [Conditionals](https://rareskills.io/post/circom-if-statement) · [Quin selector](https://rareskills.io/post/quin-selector) · [ZK-friendly hashes](https://rareskills.io/post/zk-friendly-hash) · [Permutation argument](https://rareskills.io/post/permutation-argument) · [Tornado Cash line by line](https://rareskills.io/post/how-does-tornado-cash-work)

Security and reference: zkSecurity — [Common Circom pitfalls, Part 1](https://blog.zksecurity.xyz/posts/circom-pitfalls-1/) and [Part 2](https://blog.zksecurity.xyz/posts/circom-pitfalls-2/) · [How Groth16 works (written companion)](https://blog.zksecurity.xyz/posts/pudding-10-groth16/) · [EIP-196](https://eips.ethereum.org/EIPS/eip-196) · [EIP-197](https://eips.ethereum.org/EIPS/eip-197) · [Circom docs](https://docs.circom.io/) · [circomlib](https://github.com/iden3/circomlib) · [snarkjs](https://github.com/iden3/snarkjs) · [py_ecc](https://github.com/ethereum/py_ecc) · [Understanding PLONK — David Wong](https://cryptologie.net/article/527/understanding-plonk)

### Videos

Each video below was checked in October 2026: the URL resolves, and the title, channel and description match the topic it is assigned to. Video length could not be confirmed for every entry. Videos support the reading; they never replace it.

| Week | Video | Channel | Why it's here |
|---|---|---|---|
| 1 | [What is a SNARK? (ZK Whiteboard Sessions, Module 1)](https://www.youtube.com/watch?v=h-94UhJLeck) — Dan Boneh | Zero Knowledge | The big picture before the math |
| 1 | [Lecture 11: Euclidean algorithm, Euler's phi, Euler's theorem](https://www.youtube.com/watch?v=fq6SXByItUI) — Christof Paar | Introduction to Cryptography by Christof Paar | Modular inverses, done properly |
| 2 | [Group Theory — Demystifying Cryptography Fundamentals for Developers (1/3)](https://www.youtube.com/watch?v=3N059G8H6b0) | koalateectrl | Groups, fields, discrete log for developers |
| 3 | [Lectures on Elliptic Curve Cryptography](https://www.youtube.com/watch?v=LdYtsMyPnyc) — Alfred Menezes | Cryptography 101 | Point addition, group law, Hasse's theorem |
| 3 | [PSE: a full course on ECC from scratch (playlist)](https://www.youtube.com/playlist?list=PLV91V4b0yVqQ_inAjuIB5SwBNyYmA9S6M) | Privacy Stewards of Ethereum | Optional reference; dip in when stuck |
| 4 | [Elliptic Curve Pairings — Demystifying Cryptography Fundamentals (3/3)](https://www.youtube.com/watch?v=FE70-F_wkGw) | koalateectrl | Pairings and verification, ~22 min |
| 5 | [ZK-LDN 0x01: Designing efficient R1CS circuits](https://www.youtube.com/watch?v=Uug5p05_wqs) — Daira Hopwood | Zero Knowledge | Writing R1CS directly, from Zcash's Sapling work |
| 6 | [Multivariate polynomials and the Schwartz–Zippel lemma (CMU CS Theory Toolkit 10e)](https://www.youtube.com/watch?v=Rzmj5OA-QqU) — Ryan O'Donnell | Ryan O'Donnell | The lemma that makes QAP sound |
| 7 | [Building a SNARK, pt 1 (ZK Whiteboard Sessions, Module 2)](https://www.youtube.com/watch?v=J4pVTamUBvU) — Dan Boneh | Zero Knowledge | Commitments + IOPs: where QAP fits |
| 8 | [Powers of Tau — Solidity Fridays](https://www.youtube.com/watch?v=TcQXzGTSXfo) | Solidity Fridays | The setup ceremony |
| 9 | [How Groth16 Works — Proof is in the Pudding #10](https://www.youtube.com/watch?v=8Tl20_XUZLI) — David Wong (zkSecurity) | Archetype | ~1 hour, R1CS → final verification equation |
| 9 | [Zero-Knowledge Proof: Groth16](https://www.youtube.com/watch?v=VQyDSxB9Bls) — Alexey Kalmykov | DoraHacks | Optional second explanation with a toy example |
| 10 | [ZKP MOOC Lecture 3: Programming ZKPs](https://www.youtube.com/watch?v=UpRSaG6iuks) — Pratyush Mishra & Alex Ozdemir | Berkeley RDI | ZK languages and compilers |
| 11 | [Picus: push-button ZK circuit verification](https://www.youtube.com/watch?v=4iDhdEmwnlQ) — Shankara Pailoor | EthCC | Detecting underconstrained circuits automatically |
| 11 | [Tornado Cash — How it Works](https://www.youtube.com/watch?v=z_cRicXX1jI) | Smart Contract Programmer | Commitments, nullifiers, Merkle proofs, ~12 min |
| 12 | [Build Your First ZKP — Circom + SnarkJS Full Tutorial (2025)](https://www.youtube.com/watch?v=NG2NX1cDGUs) | CodeByAnkita | The snarkjs → Solidity verifier toolchain, start to finish |
| 12 | [ZK Tutorial #1: Solidity verifiers (2022)](https://www.youtube.com/watch?v=zXHLIvIDO7w) | BattleZips | Optional: integrating snarkjs verifiers in a real dapp |
| 14 | [ZKP MOOC Lecture 2: Overview of Modern SNARK Constructions](https://www.youtube.com/watch?v=bGEXYpt3sj0) | Berkeley RDI | Where Groth16 sits among all SNARKs |
| 15 | [Building a SNARK, pt 2 (ZK Whiteboard Sessions, Module 3)](https://www.youtube.com/watch?v=vxyoPM2m7Yg) — Dan Boneh | Zero Knowledge | Polynomial IOPs, with PLONK as the example |
| 15 | [ZKP MOOC Lecture 5: The Plonk SNARK](https://www.youtube.com/watch?v=A0oZVEXav24) — Dan Boneh | Berkeley RDI | Full PLONK lecture |
| 16 | [ZKP MOOC Lecture 6: Polynomial commitments based on pairing and discrete log](https://www.youtube.com/watch?v=WyT5KkKBJUw) — Yupeng Zhang | Berkeley RDI | KZG and friends |
| 16 | [KZG Commitments (Layer 1 R&D, Devconnect 2022)](https://www.youtube.com/watch?v=g6s4zpypPT4) — Ben Edgington | Ethereum DEV NL | KZG as used in EIP-4844 |

Removed from the previous version: a YouTube **search** link (not a video), a 2019 Circom 1 tutorial (Circom 2 syntax differs), an unattributed 2022 workshop that duplicated better material, and an AES-focused Galois-field lecture (wrong field type for ZK).
