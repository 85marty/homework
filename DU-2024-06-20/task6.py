def load_file(filename):
    file = open(filename, mode="r")
    text = file.read()
    file.close()
    return text


def save_file(text, filename):
    file = open(filename, mode="w")
    file.write(text)
    file.close()


to_search = input('Which word you want to replace? ')
to_replace = input('Please input the replacement ')
filename = 'data/sample_one.txt'
save_file(load_file(filename).replace(to_search, to_replace), filename)
