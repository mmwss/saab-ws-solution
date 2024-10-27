numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum_squares_even = sum(num ** 2 for num in numbers if num % 2 == 0)
sum_cubes_odd = sum(num ** 3 for num in numbers if num % 2 != 0)

print('Sum of squares of even numbers:', sum_squares_even)
print('Sum of cubes of odd numbers:', sum_cubes_odd)
