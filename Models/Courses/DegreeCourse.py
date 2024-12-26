from abc import ABC


class DegreeCourse(ABC):
    DegreeCourseId: int
    Name: str
    StartDate: int
    ExpectedFinishDate: int
    Degree: int # enum
