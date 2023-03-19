"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """

    square_number = [x**2 for x in args]
    return square_number


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_even(number):
    return number % 2 == 0


def is_odd(number):
    return number % 2 == 1


def is_prime(number):
    k = 0
    for i in range(2, number // 2 + 1):
        if (number % i == 0):
            k = k + 1
    if k <= 0 and number != 1:
        # Число простое
        return number


def filter_numbers(num_list, type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """

    if type == EVEN:
        return list(filter(is_even, num_list))
    elif type == ODD:
        return list(filter(is_odd, num_list))
    elif type == PRIME:
        return list(filter(is_prime, num_list))
    else:
        print("Error!")
