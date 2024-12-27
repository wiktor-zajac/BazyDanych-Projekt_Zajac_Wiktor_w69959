from datetime import date
from Models.CustomModel import CustomModel 
from Models.Courses.Course import Course
from Models.Enums.AttandanceTypes import AttandanceTypes
from Models.Users.Professor import Professor
from Models.Users.Student import Student
import django.db.models as models


class CourseAttandance(CustomModel):
    CourseAttandanceId = models.AutoField(primary_key=True, editable=False, null=False, unique=True)
    StudentId = models.ForeignKey(Student, to_field=Student.StudentId)
    CourseId = models.ForeignKey(Course, to_field=Course.CourseId)
    ProfessorId = models.ForeignKey(Professor, to_field=Professor.ProfessorId)
    Date = models.DateField(null=False, default=date.today())
    Status = models.IntegerField(choices=AttandanceTypes, null=False)
