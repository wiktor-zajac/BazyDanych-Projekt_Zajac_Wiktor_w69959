from Models.CustomModel import CustomModel
from Models.Courses.Course import Course
from Models.Users.Professor import Professor
import django.db.models as models


class Professors_Courses(CustomModel):
    ProfessorId = models.ForeignKey(to=Professor, to_field=Professor.ProfessorId)
    CourseId = models.ForeignKey(to=Course, to_field=Course.CourseId)
