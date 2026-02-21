# Euler Approximation

## Overview

This project implements a Monte Carlo method to approximate Euler's number e using random sampling. The algorithm simulates the process of summing independent Uniform(0,1) random variables until the total exceeds 1, and records how many samples were required.

---

## Mathematical Explanation

Let X₁, X₂, X₃, ... be independent random variables uniformly distributed on the interval [0,1].

Define the partial sums:

Sₖ = X₁ + X₂ + ... + Xₖ

Let N be the smallest integer such that:

Sₙ > 1

A classical result states:

E[N] = e

This follows from the identity:

P(Sₖ ≤ 1) = 1 / k!

Geometrically, the region

x₁ + x₂ + ... + xₖ ≤ 1

inside the unit cube [0,1]^k is a standard k-dimensional simplex with volume 1 / k!.

Using the tail-sum formula for expectations:

E[N] = Σ (from k = 0 to ∞) P(Sₖ ≤ 1)
     = Σ (from k = 0 to ∞) 1 / k!
     = e

The simulation estimates this expectation empirically.

---

## Usage

Run from the project directory:

```bash
python3 Euler_approximation.py
```

---

## Requirements

- Python 3
- Standard library modules:
  - random
  - statistics

---

## License

MIT License

---

## Author

Pib1666
