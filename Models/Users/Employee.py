from abc import ABC


class Employee(ABC):
    ProfessorId: int
    FirstName: str
    LastName: str
    ContactInfoId: int
    PersonalInfoId: int
    ResidentialAddressId: int
    CorrespondenceAddressId: int
    Title: str
