class Book:
    __title: str or None
    __year_of_release: str or None
    __publisher: str or None
    __genre: str or None
    __author: str or None
    __price: str or None

    def __init__(self):
        self.__title = None
        self.__year_of_release = None
        self.__publisher = None
        self.__genre = None
        self.__author = None
        self.__price = None

    def set_title(self, title):
        self.__title: str = title

    def set_year_of_release(self, year_of_release):
        self.__year_of_release: str = year_of_release

    def set_publisher(self, publisher):
        self.__publisher: str = publisher

    def set_genre(self, genre):
        self.__genre: str = genre

    def set_author(self, author):
        self.__author: str = author

    def set_price(self, price):
        self.__price: str = price

    def get_title(self):
        return self.__title

    def get_year_of_release(self):
        return self.__year_of_release

    def get_publisher(self):
        return self.__publisher

    def get_genre(self):
        return self.__genre

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price
