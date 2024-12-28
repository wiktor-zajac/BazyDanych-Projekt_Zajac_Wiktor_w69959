from Models.CustomModel import DEFAULT_CHAR_FIELD_LENGTH, CustomModel
import django.db.models as models


class DegreeModule(CustomModel):
    DegreeModuleId = models.BigAutoField(primary_key=True)
    Name = models.CharField(max_length=DEFAULT_CHAR_FIELD_LENGTH)
