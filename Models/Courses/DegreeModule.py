from Models.CustomModel import CustomModel
import django.db.models as models


class DegreeModule(CustomModel):
    DegreeModuleId = models.AutoField(primary_key=True, editable=False, null=False, unique=True)
    Name = models.CharField(max_length=256, editable=True, null=False, blank=False)
