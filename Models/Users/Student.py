from abc import ABC


class Student(ABC):
    StudentId: int
    FirstName: str
    LastName: str
    ContactInfoId: int
    PersonalInfoId: int
    ResidentialAddressId: int
    CorrespondenceAddressId: int
    Title: str