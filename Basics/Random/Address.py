from dataclasses import  dataclass , asdict

@dataclass
class Address:
    street:str
    cit:str
    country:str