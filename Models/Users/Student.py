from Models.CustomModel import CustomModel
from Models.UserInfo.Address import Address
from Models.UserInfo.ContactInfo import ContactInfo
from Models.UserInfo.PersonalInfo import PersonalInfo
import django.db.models as models


class Student(CustomModel):
    StudentId = models.AutoField(primary_key=True, editable=False, null=False, unique=True)
    FirstName = models.CharField(max_length=256, editable=True, null=False, blank=False)
    LastName = models.CharField(max_length=256, editable=True, null=False, blank=False)
    ContactInfoId = models.ForeignKey(to=ContactInfo, to_field=ContactInfo.ContactInfoId)
    PersonalInfoId = models.ForeignKey(to=PersonalInfo, to_field=PersonalInfo.PersonalInfoId)
    ResidentialAddressId = models.ForeignKey(to=Address, to_field=Address.AddressId)
    CorrespondenceAddressId = models.ForeignKey(to=Address, to_field=Address.AddressId)
    Title = models.CharField(max_length=256, editable=True, null=False, blank=False)
