def load_file_lines(filename):
    file = open(filename, mode="r")
    lines = file.readlines()
    file.close()
    return lines


def save_lines(lines, filename="demo.txt"):
    file = open(filename, mode="w")
    file.writelines(lines)
    file.close()


file_lines = load_file_lines("data/sample_one.txt")
file_lines.pop()
save_lines(file_lines)
