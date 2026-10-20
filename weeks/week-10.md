# Week 10 — Circom fundamentals and design patterns

**Goal:** write correct Circom 2 circuits, and see that the R1CS Circom generates is the same thing you built by hand in Week 5.

**Reading (in order):** [Intro to Circom](https://rareskills.io/post/circom-intro) · [Hello world](https://rareskills.io/post/hello-world-circom) · [Syntax: parameters, loops, if, assert](https://rareskills.io/post/circom-syntax) · [Quadratic constraints](https://rareskills.io/post/quadratic-constraints) · [Symbolic variables](https://rareskills.io/post/circom-symbolic-variable) · [Intermediate signals and sub-components](https://rareskills.io/post/circom-intermediate-signals) · [Public and private inputs](https://rareskills.io/post/circom-public-private-inputs) · [Indicate then constrain](https://rareskills.io/post/indicate-then-constrain) · [Compute then constrain](https://rareskills.io/post/compute-then-constrain)
**Docs:** [Circom](https://docs.circom.io/) · [snarkjs](https://github.com/iden3/snarkjs) · [circomlib](https://github.com/iden3/circomlib)
**Video:** [ZKP MOOC Lecture 3: Programming ZKPs](https://www.youtube.com/watch?v=UpRSaG6iuks) (Day 1)

## Day 1 — Toolchain and hello world
- Install Circom 2 and snarkjs (see the Circom docs). Watch the Berkeley lecture.
- Read *Intro* and *Hello world*. Compile hello world, print its R1CS with `snarkjs r1cs print`, and compare it to what you would have written by hand.
- **Deliverable:** `solutions/week-10/hello/` with build commands in a README

## Day 2 — Syntax and quadratic constraints
- Read *Syntax* and *Quadratic constraints*.
- Re-implement `out = x³ + x + 5` in Circom. Confirm it compiles to exactly 2 constraints, the same as your `src/r1cs.py`. Then write `out = x⁴ − 2xy + y²` and match your Week 5 exam answer.
- **Deliverable:** both circuits + constraint counts

## Day 3 — Signals, variables, sub-components
- Read *Symbolic variables* and *Intermediate signals and sub-components*.
- Build a `Polynomial(N)` template that evaluates a degree-N polynomial with public coefficients at a private x, using a loop and intermediate signals.
- **Deliverable:** circuit + witness tests for N = 3 and N = 5

## Day 4 — Public vs private, end to end
- Read *Public and private inputs*.
- Run the full Groth16 flow for `Polynomial(3)`: powers-of-tau, circuit setup, witness, proof, verify. Then change one public input in `public.json` and confirm verification fails.
- **Deliverable:** script `solutions/week-10/run.sh` that runs it all

## Day 5 — The two core patterns
- Read *Indicate then constrain* and *Compute then constrain*.
- Write `IsZero` from scratch using a `<--` hint for the inverse and the constraints that make it sound. Then write `IsEqual` from `IsZero`. Test every edge case, including `in = 0`.
- **Deliverable:** `solutions/week-10/iszero.circom` + test inputs

## Day 6 — Exam (120 min, closed notes)
1. **Theory (30):** Explain the difference between `<--`, `<==` and `===`, and why `<--` alone is dangerous. Explain why a circuit cannot "branch".
2. **Coding (50):** Write `Max2()` that outputs the larger of two 8-bit inputs, using circomlib comparators, with a full proof/verify run and 3 valid / 2 invalid witness attempts.
3. **Debugging (20):** An `IsZero` uses `inv <-- in != 0 ? 1/in : 0; out <== -in*inv + 1;` and nothing else. Find an input and a malicious `inv` that give the wrong output, and add the missing constraint.

## Day 7 — Rest or catch up

## Exit criteria
- [ ] Full Circom → snarkjs Groth16 flow runs from one script
- [ ] Your Circom cubic compiles to the same R1CS as your hand-written one
- [ ] Can write `IsZero` correctly from memory
- [ ] Exam score in `progress.csv`
