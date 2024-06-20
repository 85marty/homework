def load_file_lines(filename):
    file = open(filename, mode="r")
    lines = file.readlines()
    file.close()
    return lines


longest = 0
longest_line_number = 0
file_lines = load_file_lines("data/sample_one.txt")
lines_count = len(file_lines)
for index in range(lines_count):
    line_number = index + 1
    line_length = len(file_lines[index])
    if longest < line_length:
        longest = line_length
        longest_line_number = line_number

print(f"The longest line is line {longest_line_number} with {longest} characters")
