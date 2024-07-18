import json
import re


class JsonFile:
    def __init__(self, path):
        self.__path = path

    def save(self, data):
        with open(self.__path, "w") as write:
            json.dump(data, write)

    def load(self):
        with open(self.__path, "r") as read:
            return json.load(read)


class Restaurant:
    __phone: str
    __website: str
    __address: str
    __specialization: str
    __name: str

    def __init__(
            self,
            name=None,
            specialization=None,
            address=None,
            website=None,
            phone=None
    ):
        self.__name = name
        self.__specialization = specialization
        self.__address = address
        self.__website = website
        self.__phone = phone

    def map(self, restaurant_data):
        self.__name = restaurant_data['name']
        self.__specialization = restaurant_data['specialization']
        self.__address = restaurant_data['address']
        self.__website = restaurant_data['website']
        self.__phone = restaurant_data['phone']

    def serialize(self):
        return {
            'name': self.__name,
            'specialization': self.__specialization,
            'address': self.__address,
            'website': self.__website,
            'phone': self.__phone
        }

    @property
    def name(self):
        return self.__name

    @property
    def specialization(self):
        return self.__specialization

    @property
    def website(self):
        return self.__website

    @property
    def phone(self):
        return self.__phone


class Restaurants:
    __restaurants: dict[str, Restaurant]

    def __init__(
            self,
    ):
        """
        :rtype: Restaurant{}
        """
        self.__restaurants = {}

    def add(self, restaurant: Restaurant):
        """
        :type restaurant: Restaurant
        """
        self.__restaurants[restaurant.name] = restaurant

    def remove(self, name):
        del self.__restaurants[name]

    def get(self, name: str):
        """
        :type name: str
        """
        return self.__restaurants[name]

    def serialize(self):
        restaurants = {}
        for key in self.__restaurants:
            restaurants[key] = self.__restaurants[key].serialize()

        return restaurants

    def map(self, data):
        self.__restaurants = {}
        for key in data:
            self.__restaurants[key] = Restaurant()
            self.__restaurants[key].map(data[key])

    def get_all(self):
        return self.__restaurants


class RestPresenter:
    __restaurants: Restaurants | None

    def __init__(
            self,
            json_file
    ):
        self.__restaurants = None
        self.__json_file = json_file
        self.__load_restaurants()

    def __load_restaurants(self):
        self.__restaurants = Restaurants()
        try:
            self.__restaurants.map(self.__json_file.load())
        except FileNotFoundError:
            print('Bude založen nový soubor s restauracemi...')

    def __save_restaurants(self):
        self.__json_file.save(self.__restaurants.serialize())

    def __add_restaurant(self):
        name = input('Jméno restaurace: ')
        specialization = input('Specializace: ')
        address = input('Adresa: ')
        website = input('Web link: ')
        phone = input('Telefon: ')

        self.__restaurants.add(Restaurant(name, specialization, address, website, phone))
        self.__save_restaurants()

    def __modify_restaurant(self, name):
        try:
            restaurant = self.__restaurants.get(name)
            restaurant_serialize = restaurant.serialize()
            edited_restaurant = {}
            for key in restaurant_serialize:
                edited_restaurant[key] = input(f"Zadejte {key} (původně {restaurant_serialize[key]}) :")
            restaurant.map(edited_restaurant)
            self.__save_restaurants()
        except KeyError:
            print('Restaurace neexistuje')

    def __search_restaurant(self, param, search):
        restaurants_serialize = self.__restaurants.serialize()
        found = False
        for key in restaurants_serialize:
            if param in restaurants_serialize[key]:
                if re.search(search, restaurants_serialize[key][param], re.IGNORECASE):
                    print(restaurants_serialize[key])
                    found = True
            else:
                print('Neexistující parametr')
                return
        if not found:
            print('Řetězec nenalezen')

    def __display_all(self):
        print(self.__restaurants.serialize())

    @staticmethod
    def __show_menu():
        print("1 pridat restauraci")
        print("2 smazat restauraci")
        print("3 vypsat restaurace")
        print("4 upravit restauraci")
        print("5 hledat podle parametru")
        print("k konec")
        return input("Zadej volbu ")

    def run(self):
        choice = None
        while choice != 'K':
            choice = RestPresenter.__show_menu()
            match choice:
                case '1':
                    self.__add_restaurant()
                case '2':
                    self.__restaurants.remove(input('Zadejte jméno pro smazání: '))
                case '3':
                    self.__display_all()
                case '4':
                    self.__modify_restaurant(input('Zadejte jméno restaurace pro úpravu: '))
                case '5':
                    self.__search_restaurant(input('Zadej název parametru: '), input('Zadej hledaný řetězec: '))
                case 'k':
                    continue
                case 'K':
                    continue
                case _:
                    print('Neplatná volba')


presenter = RestPresenter(JsonFile('rest_data'))
presenter.run()
