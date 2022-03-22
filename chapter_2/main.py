def simple_sigma(max_number):
    total = 0
    for i in range(max_number + 1):
        total += i
    return total


def difficult_sigma(upper):
    total = 0
    for i in range(upper + 1):
        total += (i ** 2 + 1)
    return total


def average(numbers):
    return sum(numbers) / len(numbers)
