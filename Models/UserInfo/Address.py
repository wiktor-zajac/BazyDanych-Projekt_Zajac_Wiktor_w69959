from abc import ABC


class Address(ABC):
    AddressId: int
    PostalCode: str
    City: str
    PostalOffice: str
    Address: str
