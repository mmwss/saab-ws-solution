"""
Generates the Fibonacci sequence up to the n-th term.

Complete the implementation of a function generate_fibonacci(n) that returns a list containing the Fibonacci sequence up to the n-th term.
"""

def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    sequence = [0, 1]
    for i in range(2, n):
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
    return sequence

# Example usage
if __name__ == "__main__":
    print("Code Completion[1] Fibonacci Sequence Generator")

    n_terms = 10
    fib_sequence = generate_fibonacci(n_terms)

    print(f"Fibonacci sequence up to {n_terms} terms: {fib_sequence}")
