from Models.CustomModel import CustomModel
import django.db.models as models


class ContactInfo(CustomModel):
    ContactInfoId = models.AutoField(primary_key=True, editable=False, null=False, unique=True)
    PrimaryPhoneNumber = models.CharField(max_length=256, editable=True, null=False, blank=False)
    SecondaryPhoneNumber = models.CharField(max_length=256, editable=True, null=False, blank=False)
    PrimaryEmail = models.CharField(max_length=256, editable=True, null=False, blank=False)
    SecondaryEmail = models.CharField(max_length=256, editable=True, null=False, blank=False)
