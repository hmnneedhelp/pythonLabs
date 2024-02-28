def split_even_odd(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]
    return even_numbers, odd_numbers

numbers = []
start = int(input("Введите начальное значение списка: "))
end = int(input("Введите конечное значение списка: "))

for num in range(start, end + 1):
    numbers.append(num)

even_nums, odd_nums = split_even_odd(numbers)

print("Список четных чисел:", even_nums)
print("Список нечетных чисел:", odd_nums)
