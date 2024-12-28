from Models.CustomModel import DEFAULT_CHAR_FIELD_LENGTH, CustomModel
import django.db.models as models


class Address(CustomModel):
    AddressId = models.BigAutoField(primary_key=True)
    PostalCode = models.CharField(max_length=DEFAULT_CHAR_FIELD_LENGTH)
    City = models.CharField(max_length=DEFAULT_CHAR_FIELD_LENGTH)
    PostalOffice = models.CharField(max_length=DEFAULT_CHAR_FIELD_LENGTH)
    Address = models.CharField(max_length=DEFAULT_CHAR_FIELD_LENGTH)
