from Models.CustomModel import CustomModel
import django.db.models as models


class PersonalInfo(CustomModel):
    PersonalInfoId = models.AutoField(primary_key=True, editable=False, null=False, unique=True)
    DateOfBirth = models.DateField(null=False)
    PESEL = models.CharField(max_length=11, editable=True, null=False, blank=False)
    IdentificationDocument = models.CharField(max_length=256, editable=True, null=False, blank=False)
    Sex = models.CharField(max_length=1, editable=True, null=False, blank=False)
    FathersName = models.CharField(max_length=256, editable=True, null=False, blank=False)
    MothersName = models.CharField(max_length=256, editable=True, null=False, blank=False)
