from Models.CustomModel import DEFAULT_CHAR_FIELD_LENGTH, CustomModel
import django.db.models as models


class PersonalInfo(CustomModel):
    PersonalInfoId = models.BigAutoField(primary_key=True)
    DateOfBirth = models.DateField()
    PESEL = models.CharField(max_length=11)
    IdentificationDocument = models.CharField(max_length=DEFAULT_CHAR_FIELD_LENGTH)
    FathersName = models.CharField(max_length=DEFAULT_CHAR_FIELD_LENGTH)
    MothersName = models.CharField(max_length=DEFAULT_CHAR_FIELD_LENGTH)
