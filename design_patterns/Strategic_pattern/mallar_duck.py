from design_patterns.Strategic_pattern.abstract.duck import Duck
from design_patterns.Strategic_pattern.abstract.flyable import Flyable
from design_patterns.Strategic_pattern.abstract.quackable import Quackable


class Mallar_duck(Duck, Flyable , Quackable):

    def display(self):
        print("I am display method from class {0}".format(self.__class__.__name__))

    def quack(self):
        print("quack method from class {0}".format(self.__class__.__name__))

    def swim(self):
        print("swim method from class {0}".format(self.__class__.__name__))

    def fly(self):
        print("fly method from class {c}".format(c = self.__class__.__name__))