from Models.CustomModel import CustomModel
from Models.Users.Student import Student
import django.db.models as models


class Payment(CustomModel):
    PaymentId = models.AutoField(primary_key=True, editable=False, null=False, unique=True)
    Cost: str # TBD
    Paid: str # TBD
    Currency: str # TBD
    DueDate = models.DateField(null=False)
    PaidDate = models.DateField(null=False)
    Title = models.CharField(max_length=256, editable=True, null=False, blank=False)
    StudentId = models.ForeignKey(to=Student, to_field=Student.StudentId)
