from abc import ABC, abstractmethod


class Duck(ABC):

    @abstractmethod
    def swim(self):
        pass

    @abstractmethod
    def display(self):
        pass
