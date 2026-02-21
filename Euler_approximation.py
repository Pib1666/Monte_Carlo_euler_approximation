import random
import statistics

def euler_approximation(n):
    count = []
    for i in range(n):
        total = 0
        count_iterations = 0
        while total <= 1:
            total += random.uniform(0, 1)
            count_iterations += 1
        count.append(count_iterations)
    return statistics.mean(count)

if __name__ == "__main__":
    n = 100000
    print("Script started")
    e_approx = euler_approximation(n)
    print(f"Approximation of Euler's number with {n} iterations: {e_approx}")