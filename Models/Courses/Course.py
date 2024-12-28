from Models.CustomModel import DEFAULT_CHAR_FIELD_LENGTH, CustomModel
from Models.Courses.DegreeModule import DegreeModule
from Models.Enums.GradeTypes import GradeTypes
import django.db.models as models
from django.core.validators import MinValueValidator


class Course(CustomModel):
    CourseId = models.BigAutoField(primary_key=True)
    Name = models.CharField(max_length=DEFAULT_CHAR_FIELD_LENGTH)
    GradeType = models.IntegerField(choices=GradeTypes, default=GradeTypes.RegularGrade)
    ECTS = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    DegreeModuleId = models.ForeignKey(to=DegreeModule, to_field=DegreeModule.DegreeModuleId)
