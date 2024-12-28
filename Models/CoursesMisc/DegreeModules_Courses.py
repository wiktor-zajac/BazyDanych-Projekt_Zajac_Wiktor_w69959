from Models.CustomModel import CustomModel
from Models.Courses.DegreeModule import DegreeModule
from Models.Courses.Course import Course
import django.db.models as models


class DegreeModules_Courses(CustomModel):
    DegreeModuleId = models.ForeignKey(to=DegreeModule, to_field=DegreeModule.DegreeModuleId)
    CourseId = models.ForeignKey(to=Course, to_field=Course.CourseId)
