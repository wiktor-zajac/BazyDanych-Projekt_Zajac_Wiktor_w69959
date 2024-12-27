from Models.CustomModel import CustomModel
import django.db.models as models


class Address(CustomModel):
    AddressId = models.AutoField(primary_key=True, editable=False, null=False, unique=True)
    PostalCode = models.CharField(max_length=256, editable=True, null=False, blank=False)
    City = models.CharField(max_length=256, editable=True, null=False, blank=False)
    PostalOffice = models.CharField(max_length=256, editable=True, null=False, blank=False)
    Address = models.CharField(max_length=256, editable=True, null=False, blank=False)
