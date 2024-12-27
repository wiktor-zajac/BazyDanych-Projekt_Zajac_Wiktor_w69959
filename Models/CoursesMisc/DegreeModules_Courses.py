from Models.CustomModel import CustomModel
from Models.Courses.Course import Course
from Models.Courses.DegreeModule import DegreeModule
import django.db.models as models


class Courses_DegreeModules(CustomModel):
    DegreeModuleId = models.ForeignKey(to=DegreeModule, to_field=DegreeModule.DegreeModuleId)
    CourseId = models.ForeignKey(to=Course, to_field=Course.CourseId)
