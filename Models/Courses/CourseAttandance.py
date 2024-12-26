from abc import ABC


class CourseAttandance(ABC):
    CourseAttandanceId: int
    StudentId: str
    CourseId: int
    ProfessorId: int
    Date: int
    Status: int
