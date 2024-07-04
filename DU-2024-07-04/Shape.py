from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    def show(self):
        return '';

    def save(self):
        return '';

    def load(self):
        return '';
