def read_numbers_from_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    numbers = []
    for line in lines:
        line = line.strip()
        if line:
            try:
                num = float(line)
                numbers.append(num)
            except ValueError:
                print(f"Warning: '{line}' is not a valid number and will be skipped.")
    return numbers

def calculate_average(numbers):
    if not numbers:
        return None
    total = sum(numbers)
    average = total / len(numbers)
    return average

numbers = read_numbers_from_file('data/numbers.txt')
average = calculate_average(numbers)
if average is not None:
    print('The average is:', average)
else:
    print('No valid numbers were provided.')
