from Models.CustomModel import DEFAULT_CHAR_FIELD_LENGTH, CustomModel
from Models.UserInfo.Address import Address
from Models.UserInfo.ContactInfo import ContactInfo
from Models.UserInfo.PersonalInfo import PersonalInfo
import django.db.models as models


class Student(CustomModel):
    StudentId = models.BigAutoField(primary_key=True)
    FirstName = models.CharField(max_length=DEFAULT_CHAR_FIELD_LENGTH)
    LastName = models.CharField(max_length=DEFAULT_CHAR_FIELD_LENGTH)
    ContactInfoId = models.ForeignKey(to=ContactInfo, to_field=ContactInfo.ContactInfoId, on_delete=models.CASCADE)
    PersonalInfoId = models.ForeignKey(to=PersonalInfo, to_field=PersonalInfo.PersonalInfoId, on_delete=models.CASCADE)
    ResidentialAddressId = models.ForeignKey(to=Address, to_field=Address.AddressId, on_delete=models.CASCADE)
    CorrespondenceAddressId = models.ForeignKey(to=Address, to_field=Address.AddressId, on_delete=models.CASCADE)
    Title = models.CharField(max_length=DEFAULT_CHAR_FIELD_LENGTH)
