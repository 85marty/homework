def calc_power(number, power):
    if power == 0:
        return 1
    return number * calc_power(number, power - 1)


def list_power(numbers, power):
    powered = []
    for number in numbers:
        powered.append(calc_power(number, power))
    return powered
