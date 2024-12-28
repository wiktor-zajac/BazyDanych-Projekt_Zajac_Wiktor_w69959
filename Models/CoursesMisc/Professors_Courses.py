from Models.CustomModel import CustomModel
from Models.Courses.Course import Course
from Models.Users.Profesor import Profesor
import django.db.models as models


class Profesors_Courses(CustomModel):
    ProfesorId = models.ForeignKey(to=Profesor, to_field=Profesor.ProfesorId)
    CourseId = models.ForeignKey(to=Course, to_field=Course.CourseId)
