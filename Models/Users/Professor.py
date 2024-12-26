from abc import ABC


class Professor(ABC):
    ProfessorId: int
    FirstName: str
    LastName: str
    ContactInfoId: int
    PersonalInfoId: int
    ResidentialAddressId: int
    CorrespondenceAddressId: int
    Title: str
