class Dictionary:
    def __init__(self):
        self.dict = {}
        self.popularity_counter = {}

    def replace_in_dict(self, key, value):
        self.search_in_dict(key)
        self.dict |= {key: value}

    def delete_from_dict(self, key):
        self.search_in_dict(key)
        del self.dict[key]

    def search_in_dict(self, key):
        try:
            result = self.dict[key]
        except KeyError:
            print("Key " + key + " not exist")
            return

        try:
            self.popularity_counter[key] += 1
        except KeyError:
            self.popularity_counter[key] = 1

        return result

    def add_to_dict(self, key, value):
        self.dict[key] = value

    def get_most_popular(self, count):
        print(self.__sort(self.popularity_counter, True))

    def get_most_unpopular(self, count):
        print(self.__sort(self.popularity_counter))

    @staticmethod
    def __sort(words, desc=False):
        """
        :param words: {items}
        :type desc: bool
        """
        return dictionary(sorted(words.items(), key=lambda item: item[1], reverse=desc))


def print_menu():
    print("1 pridat slovo")
    print("2 smazat slovo")
    print("3 prelozit")
    print("4 upravit preklad")
    print("5 Zobrazit 10 nejoblíbenějších")
    print("6 Zobrazit 10 nejméně oblíbených")
    print("k konec")
    return input("Zadej volbu ")


def get_en():
    return input('Zadej slovo anglicky ')


def get_fr():
    return input('Zadej slovo francouzsky ')


dictionary = Dictionary()
choice = None
my_db = []
print_menu()
while choice != 'K':
    choice = print_menu()
    match choice:
        case 1:
            dictionary.add_to_dict(get_en(), get_fr())
        case 2:
            dictionary.delete_from_dict(get_en())
        case 3:
            dictionary.search_in_dict(get_en())
        case 4:
            dictionary.replace_in_dict(get_en(), get_fr())
        case 5:
            dictionary.get_most_popular()
        case 6:
            dictionary.get_most_unpopular()
        case 'k':
            continue
        case 'K':
            continue
        case _:
            print('Neplatna volba')
