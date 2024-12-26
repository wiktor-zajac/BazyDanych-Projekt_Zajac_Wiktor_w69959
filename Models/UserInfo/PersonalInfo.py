from abc import ABC


class PersonalInfo(ABC):
    PersonalInfoId: int
    DateOfBirth: int
    PESEL: str
    IdentificationDocument: str
    Sex: str
    FathersName: str
    MothersName: str
