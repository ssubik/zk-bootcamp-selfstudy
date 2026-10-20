# Week 8: Trusted setup and Pinocchio

**Objectives:** toxic waste, powers of tau, knowledge assumptions, Pinocchio overview.

**Reading:** [RareSkills ZK Book](https://rareskills.io/zk-book) — locate chapters by the topic keywords above.

**Video:** [Trusted setup and Pinocchio lectures and walkthroughs](https://www.youtube.com/results?search_query=trusted%20setup%20Pinocchio%20zk%20SNARK) (search results; select a rigorous explanation).

## Daily schedule

### Day 1
Read the RareSkills ZK Book sections covering toxic waste; write a one-page explanation and define 5 terms.

**Deliverable:** commit your work under `solutions/week-08/day-1/` and record progress in `progress.csv`.

### Day 2
Watch [relevant lectures](https://www.youtube.com/results?search_query=trusted%20setup%20Pinocchio%20zk%20SNARK); reproduce one derivation without notes.

**Deliverable:** commit your work under `solutions/week-08/day-2/` and record progress in `progress.csv`.

### Day 3
Implement a minimal Python example for toxic waste; add at least 3 deterministic tests.

**Deliverable:** commit your work under `solutions/week-08/day-3/` and record progress in `progress.csv`.

### Day 4
Extend the implementation to cover powers of tau; test 2 edge cases and one deliberately invalid input.

**Deliverable:** commit your work under `solutions/week-08/day-4/` and record progress in `progress.csv`.

### Day 5
Explain how trusted setup and pinocchio connects to proof correctness or Solidity verification; refactor and document the code.

**Deliverable:** commit your work under `solutions/week-08/day-5/` and record progress in `progress.csv`.

### Day 6
**Timed mock exam (120 min, 100 points):** 30 points: derive/explain two core concepts; 50 points: implement a fresh variant of this week's exercise with tests; 20 points: debug a deliberately broken implementation and explain the vulnerability.

**Deliverable:** commit your work under `solutions/week-08/day-6/` and record progress in `progress.csv`.

### Day 7 — Rest or catch-up

## Weekly exam rubric

- Theory (30): correctness of definitions, derivations, and assumptions.
- Coding (50): functional correctness (30), edge cases (10), tests and clarity (10).
- Debugging (20): identify error (10), explain impact (10).

**Pass:** 75/100. **Distinction:** 90/100. Retake after reviewing errors; do not simply copy the original answer.

**Reflection:** Which assumption was hardest to justify? What fails if the witness or inputs are malformed?
