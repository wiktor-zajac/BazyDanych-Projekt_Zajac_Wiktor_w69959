from Models.CustomModel import DEFAULT_CHAR_FIELD_LENGTH, CustomModel
from Models.Enums.EducationLevels import EducationLevels
import django.db.models as models


class DegreeCourse(CustomModel):
    DegreeCourseId = models.BigAutoField(primary_key=True)
    Name = models.CharField(max_length=DEFAULT_CHAR_FIELD_LENGTH)
    StartDate = models.DateField()
    ExpectedFinishDate = models.DateField()
    Degree = models.IntegerField(choices=EducationLevels, default=EducationLevels.UNKNOWN)
