from abc import ABC


class Course(ABC):
    CourseId: int
    Name: str
    GradeType: int # enum
    ECTS: int
    DegreeModuleId: int
