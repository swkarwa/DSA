from design_patterns.Strategic_pattern.abstract.duck import Duck
from design_patterns.Strategic_pattern.abstract.quackable import Quackable


class Red_head_duck(Duck,Quackable):

    def display(self):
        print("I am display method from class {0}".format(self.__class__.__name__))

    def quack(self):
        print("quack method from class {0}".format(self.__class__.__name__))

    def swim(self):
        print("swim method from class {0}".format(self.__class__.__name__))