"""
You are given a Python script intended to read a text file containing numbers,
calculate the average, and print the result.
However, the script is not working as expected.
Your task is to use an AI debugging tool to identify and fix the issues in the code.
"""

def read_numbers_from_file(file_path):
    with open(file_path, 'r') as f:
        numbers = f.read().split('\n')
    return numbers

def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    average = total / len(numbers)
    return average

numbers = read_numbers_from_file('data/numbers.txt')
average = calculate_average(numbers)
print('The average is:', average)
