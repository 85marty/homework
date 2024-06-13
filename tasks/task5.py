def array_merge(list_one, list_two):
    for number in list_two:
        if number in list_one:
            continue
        list_one.append(number)
    return list_one


print(array_merge([1, 3, 5, 7, 9, 11], [0, 1, 2, 4, 6, 8, 10]))
