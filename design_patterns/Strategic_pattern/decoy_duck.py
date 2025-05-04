from design_patterns.Strategic_pattern.abstract.duck import Duck
from design_patterns.Strategic_pattern.abstract.flyable import Flyable


class Decoy_duck(Duck):

    def swim(self):
        print("swim method from class {c}".format(c = self.__class__.__name__))

    def display(self):
        print("display from class {c}".format(c = self.__class__.__name__))