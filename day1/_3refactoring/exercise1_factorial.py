"""
Refactor the recursive factorial function to use iteration instead,
improving efficiency and avoiding maximum recursion depth issues.
"""

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Example usage
if __name__ == "__main__":
    print("Code Refactoring[1] Factorial Calculator")
    number = 5
    print(f"The factorial of {number} is: {factorial(number)}")
