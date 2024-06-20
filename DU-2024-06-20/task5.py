def load_file(filename):
    file = open(filename, mode="r")
    text = file.read()
    file.close()
    return text


to_search = input('Which word you search? ')
print(f"Text contains {load_file('data/sample_one.txt').count(to_search)} occurrences of word {to_search}")
