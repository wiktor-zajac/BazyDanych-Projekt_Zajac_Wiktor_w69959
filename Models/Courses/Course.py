from Models.CustomModel import CustomModel
from Models.Courses.DegreeModule import DegreeModule
from Models.Enums.GradeTypes import GradeTypes
import django.db.models as models


class Course(CustomModel):
    CourseId = models.AutoField(primary_key=True, editable=False, null=False, unique=True)
    Name = models.CharField(max_length=256, editable=True, null=False, blank=False)
    GradeType = models.IntegerField(choices=GradeTypes, null=False, default=GradeTypes.RegularGrade)
    ECTS = models.IntegerField(min=0, max=100, default=0)
    DegreeModuleId = models.ForeignKey(DegreeModule, to_field=DegreeModule.DegreeModuleId)
