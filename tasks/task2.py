def minimum(numbers):
    mini = None
    for number in numbers:
        if mini is None or mini > number:
            mini = number

    return mini
