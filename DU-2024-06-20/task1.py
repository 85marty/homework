def load_file_lines(filename):
    file = open(filename, mode="r")
    lines = file.readlines()
    file.close()
    return lines


def compare_lines(sample_one, sample_two):
    length = len(sample_one) if len(sample_one) > len(sample_two) else len(sample_two)
    identical = True
    for index in range(length):
        line_number = index + 1
        try:
            sample_one_line = sample_one[line_number]
        except IndexError:
            sample_one_line = 'UNDEFINED\n'
        try:
            sample_two_line = sample_two[line_number]
        except IndexError:
            sample_two_line = 'UNDEFINED\n'

        if sample_one_line == sample_two_line:
            continue

        identical = False

        print(f"Line {line_number} have divergent texts.")
        print(f"A side: {sample_one_line}", end=" ")
        print(f"B side: {sample_two_line}", end=" ")
    if identical:
        print('Files have identical content')


compare_lines(load_file_lines("data/sample_one.txt"), load_file_lines("data/sample_two.txt"))
