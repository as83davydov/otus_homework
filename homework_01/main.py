"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*nums):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [num * num for num in nums]

# print (power_numbers(1, 2, 5, 7))

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(n):
    if n <= 1:
        return False
    for i in range (2, int(n ** (0.5)) + 1):
        if n % i == 0:
            return False
    return True

def filter_numbers(numbers, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """

    # version 1

    #filtered_numbers = []
    #if filter_type == ODD:
    #    for number in numbers:
    #        if number % 2 != 0:
    #            filtered_numbers.append(number)
    #elif filter_type == EVEN:
    #    for number in numbers:
    #        if number % 2 == 0:
    #            filtered_numbers.append(number)
    #else:
    #    for number in numbers:
    #        if is_prime(number):
    #            filtered_numbers.append(number)
    #return filtered_numbers

    # version 2

    if filter_type == ODD:
        return list(filter(lambda number: number % 2 != 0, numbers))
    elif filter_type == EVEN:
        return list(filter(lambda number: number % 2 == 0, numbers))
    else:
        return list(filter(is_prime, numbers))

