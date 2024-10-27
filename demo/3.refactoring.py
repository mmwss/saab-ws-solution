"""
You are given a Python script that processes
a list of numbers to calculate the sum of squares of even numbers
and the sum of cubes of odd numbers.
The script works correctly but is inefficient and does not follow best coding practices.
Your task is to refactor the code using an AI code refactoring tool to improve its readability,
efficiency, and maintainability.
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum_squares_even = 0
sum_cubes_odd = 0

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        sum_squares_even = sum_squares_even + numbers[i] * numbers[i]
    else:
        sum_cubes_odd = sum_cubes_odd + numbers[i] * numbers[i] * numbers[i]

print('Sum of squares of even numbers:', sum_squares_even)
print('Sum of cubes of odd numbers:', sum_cubes_odd)
