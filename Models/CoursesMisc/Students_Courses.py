from abc import ABC


class Students_Courses(ABC):
    StudentId: int
    CourseId: str
    Grade: int # enum
    Term: int
    AssignedBy: int # FK to Professor
