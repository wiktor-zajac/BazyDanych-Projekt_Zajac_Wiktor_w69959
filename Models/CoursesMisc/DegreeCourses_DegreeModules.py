from Models.CustomModel import CustomModel
from Models.Courses.DegreeModule import DegreeModule
from Models.Courses.DegreeCourse import DegreeCourse
import django.db.models as models


class DegreeCourses_DegreeModules(CustomModel):
    DegreeCourseId = models.ForeignKey(to=DegreeCourse, to_field=DegreeCourse.DegreeCourseId)
    DegreeModuleId = models.ForeignKey(to=DegreeModule, to_field=DegreeModule.DegreeModuleId)
