from abc import ABC


class ContactInfo(ABC):
    ContactInfoId: int
    PrimaryPhoneNumber: str
    SecondaryPhoneNumber: str
    PrimaryEmail: str
    SecondaryEmail: str
