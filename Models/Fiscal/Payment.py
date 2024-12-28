from Models.CustomModel import DEFAULT_CHAR_FIELD_LENGTH, CustomModel
from Models.Users.Student import Student
import django.db.models as models


class Payment(CustomModel):
    PaymentId = models.BigAutoField(primary_key=True)
    Cost: str # TBD
    Paid: str # TBD
    Currency: str # TBD
    DueDate = models.DateField()
    PaidDate = models.DateField()
    Title = models.CharField(max_length=DEFAULT_CHAR_FIELD_LENGTH)
    StudentId = models.ForeignKey(to=Student, to_field=Student.StudentId)
