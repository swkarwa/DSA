from dataclasses import  dataclass

from Basics.Random.Address import Address


@dataclass
class Person:
    first_name:str
    last_name:str
    address: Address