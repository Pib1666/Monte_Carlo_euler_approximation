# Euler Approximation

## Overview
This project implements a Monte Carlo method to approximate Euler's number (e) using random sampling. The algorithm simulates the process of summing random numbers until the total exceeds 1, counting the number of iterations required for each simulation.

## Features
- Monte Carlo simulation for approximating Euler's number
- Utilizes Python's `random` and `statistics` libraries
- High iteration count for improved accuracy

## Installation
To run this project, you need to have Python 3 installed.

## Usage
To use the Euler approximation method, run the following command:
```bash
python3 Euler_approximation.py
```

## Example Output
The script will output the approximation of Euler's number based on the specified number of iterations.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Author
Pib1666

## Mathematical Explanation for the Algorithm

Let $X_1, X_2, \ldots$ be independent random variables uniformly distributed on the interval $[0, 1]$.  

Define the partial sums  
$$S_k = X_1 + X_2 + \cdots + X_k.$$  

Let $N$ be the smallest integer such that $S_N > 1$.  

A classical result states:  
$$E[N] = e.$$  

This follows from the identity  
$$P(S_k \leq 1) = \frac{1}{k!},$$  

since the region $\\{x_1 + \cdots + x_k \leq 1\} \subset [0, 1]^k$ is a standard $k$-simplex with volume $rac{1}{k!}$. Using the tail-sum formula for expectations,  
$$E[N] = \sum_{k=0}^{\infty} P(S_k \leq 1) = \sum_{k=0}^{\infty} \frac{1}{k!} = e.$$  

The simulation approximates this expectation empirically.

