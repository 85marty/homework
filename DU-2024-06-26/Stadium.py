class Stadium:
    __name: str or None
    __date_of_opening: str or None
    __country: str or None
    __city: str or None
    __seating_capacity: str or None

    def __init__(self):
        self.__name = None
        self.__date_of_opening = None
        self.__country = None
        self.__city = None
        self.__seating_capacity = None

    def set_name(self, name):
        self.__name: str = name

    def set_date_of_opening(self, date_of_opening):
        self.__date_of_opening: str = date_of_opening

    def set_country(self, country):
        self.__country: str = country

    def set_city(self, city):
        self.__city: str = city

    def set_seating_capacity(self, seating_capacity):
        self.__seating_capacity: str = seating_capacity

    def get_name(self):
        return self.__name

    def get_date_of_opening(self):
        return self.__date_of_opening

    def get_country(self):
        return self.__country

    def get_city(self):
        return self.__city

    def get_seating_capacity(self):
        return self.__seating_capacity

