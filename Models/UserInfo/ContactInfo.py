from Models.CustomModel import DEFAULT_CHAR_FIELD_LENGTH, CustomModel
import django.db.models as models


class ContactInfo(CustomModel):
    ContactInfoId = models.BigAutoField(primary_key=True)
    PrimaryPhoneNumber = models.CharField(max_length=15)
    SecondaryPhoneNumber = models.CharField(max_length=15)
    PrimaryEmail = models.EmailField(max_length=DEFAULT_CHAR_FIELD_LENGTH)
    SecondaryEmail = models.EmailField(max_length=DEFAULT_CHAR_FIELD_LENGTH)
