# Week 10: Circom and snarkjs

**Objectives:** signals, templates, component constraints, witness generation, test vectors.



## Curated primary resources

**Direct RareSkills chapters** (specific articles, not searches):
- [Introduction to Circom](https://rareskills.io/post/circom-intro)
- [Hello World Circom](https://rareskills.io/post/hello-world-circom)

**Direct YouTube videos** (verified titles/URLs from indexed metadata; applicability varies):
- [BattleZips: Circom tutorial](https://www.youtube.com/watch?v=PyLwC7GaZY8)
- [Christian Lacdael: Circom/snarkjs example](https://www.youtube.com/watch?v=2BHdTjpYmFg)

**Source note:** Videos are supplementary and not presented as RareSkills bootcamp recordings. Chapters should be read in the order listed. Video links are provided only when an identifiable relevant recording was found.

## Daily schedule

### Day 1
Read the RareSkills ZK Book sections covering signals; write a one-page explanation and define 5 terms.

**Deliverable:** commit your work under `solutions/week-10/day-1/` and record progress in `progress.csv`.

### Day 2
Watch [relevant lectures](https://www.youtube.com/results?search_query=Circom%20snarkjs%20tutorial); reproduce one derivation without notes.

**Deliverable:** commit your work under `solutions/week-10/day-2/` and record progress in `progress.csv`.

### Day 3
Implement a minimal Python example for signals; add at least 3 deterministic tests.

**Deliverable:** commit your work under `solutions/week-10/day-3/` and record progress in `progress.csv`.

### Day 4
Extend the implementation to cover templates; test 2 edge cases and one deliberately invalid input.

**Deliverable:** commit your work under `solutions/week-10/day-4/` and record progress in `progress.csv`.

### Day 5
Explain how circom and snarkjs connects to proof correctness or Solidity verification; refactor and document the code.

**Deliverable:** commit your work under `solutions/week-10/day-5/` and record progress in `progress.csv`.

### Day 6
**Timed mock exam (120 min, 100 points):** 30 points: derive/explain two core concepts; 50 points: implement a fresh variant of this week's exercise with tests; 20 points: debug a deliberately broken implementation and explain the vulnerability.

**Deliverable:** commit your work under `solutions/week-10/day-6/` and record progress in `progress.csv`.

### Day 7 — Rest or catch-up

## Weekly exam rubric

- Theory (30): correctness of definitions, derivations, and assumptions.
- Coding (50): functional correctness (30), edge cases (10), tests and clarity (10).
- Debugging (20): identify error (10), explain impact (10).

**Pass:** 75/100. **Distinction:** 90/100. Retake after reviewing errors; do not simply copy the original answer.

**Reflection:** Which assumption was hardest to justify? What fails if the witness or inputs are malformed?
