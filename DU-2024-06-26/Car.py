class Car:
    __price: str or None
    __color: str or None
    __engine_capacity: str or None
    __manufacturer: str or None
    __year_of_release: str or None
    __model: str or None

    def __init__(self):
        self.__price = None
        self.__color = None
        self.__engine_capacity = None
        self.__manufacturer = None
        self.__year_of_release = None
        self.__model = None

    def set_price(self, price):
        self.__price: str = price

    def set_color(self, color):
        self.__color: str = color

    def set_engine_capacity(self, engine_capacity):
        self.__engine_capacity: str = engine_capacity

    def set_manufacturer(self, manufacturer):
        self.__manufacturer: str = manufacturer

    def set_year_of_release(self, year_of_release):
        self.__year_of_release: str = year_of_release

    def set_model(self, model):
        self.__model: str = model

    def get_price(self):
        return self.__price

    def get_color(self):
        return self.__color

    def get_engine_capacity(self):
        return self.__engine_capacity

    def get_manufacturer(self):
        return self.__manufacturer

    def get_year_of_release(self):
        return self.__year_of_release

    def get_model(self):
        return self.__model
