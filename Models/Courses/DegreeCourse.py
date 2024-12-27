from Models.CustomModel import CustomModel
from Models.Enums.EducationLevels import EducationLevels
import django.db.models as models


class DegreeCourse(CustomModel):
    DegreeCourseId = models.AutoField(primary_key=True, editable=False, null=False, unique=True)
    Name = models.CharField(max_length=256, editable=True, null=False, blank=False)
    StartDate = models.DateField(null=False)
    ExpectedFinishDate = models.DateField(null=False)
    Degree = models.IntegerField(choices=EducationLevels)
