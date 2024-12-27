from Models.CustomModel import CustomModel
from Models.Courses.Course import Course
from Models.Users.Professor import Professor
from Models.Users.Student import Student
import django.db.models as models


class Students_Courses(CustomModel):
    StudentId = models.ForeignKey(to=Student, to_field=Student.StudentId)
    CourseId = models.ForeignKey(to=Course, to_field=Course.CourseId)
    Grade = models.IntegerField(null=True)
    Term = models.IntegerField(null=True)
    AssignedBy = models.ForeignKey(to=Professor, to_field=Professor.ProfessorId)
