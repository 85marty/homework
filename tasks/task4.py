def remove_number(numbers, remove):
    removed = 0
    for number in numbers:
        if number == remove:
            removed += 1
    if removed != 0:
        numbers.remove(remove)

    return removed
