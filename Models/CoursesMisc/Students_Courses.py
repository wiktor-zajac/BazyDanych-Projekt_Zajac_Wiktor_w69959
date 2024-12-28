from Models.CustomModel import CustomModel
from Models.Courses.Course import Course
from Models.Users.Student import Student
from Models.Users.Profesor import Profesor
import django.db.models as models
from django.core.validators import MinValueValidator


class Students_Courses(CustomModel):
    StudentId = models.ForeignKey(to=Student, to_field=Student.StudentId)
    CourseId = models.ForeignKey(to=Course, to_field=Course.CourseId)
    Grade = models.IntegerField(null=True)
    Term = models.IntegerField(null=True, validators=[MinValueValidator(0)])
    AssignedBy = models.ForeignKey(to=Profesor, to_field=Profesor.ProfesorId)
