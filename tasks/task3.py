def is_prime_number(number) -> bool:
    for search in range(number):
        if search == 0 or search == 1 or search == number:
            continue
        if number % search == 0:
            return False
    return True


def count_of_prime_number_in_list(numbers) -> int:
    count = 0
    for number in numbers:
        if is_prime_number(number):
            count += 1

    return count


print(count_of_prime_number_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
