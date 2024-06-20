def load_file_lines(filename):
    file = open(filename, mode="r")
    lines = file.readlines()
    file.close()
    return lines


characters = 0
vowels = 0
vowels_def = ['a', 'e', 'i', 'o', 'u', 'y']
consonants = 0
numbers = 0

file_lines = load_file_lines("data/sample_three.txt")
lines = len(file_lines)
for line in file_lines:
    characters += len(line)
    for char in line:
        if char in vowels_def:
            vowels += 1
        elif char.isnumeric():
            numbers += 1
        else:
            consonants += 1

print(f"lines {lines}")
print(f"characters {characters}")
print(f'vowels {vowels}')
print(f"consonants {consonants}")
print(f"numbers {numbers}")
