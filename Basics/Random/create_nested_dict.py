from dataclasses import asdict

from Basics.Random.Address import Address
from Basics.Random.Person import Person

address = Address("shrey_nagar" , "Aurangabad", "India")
person = Person("swapnil" , "karwa" , address)
print(asdict(person))