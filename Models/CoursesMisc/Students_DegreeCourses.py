from Models.CustomModel import CustomModel
from Models.Courses.DegreeCourse import DegreeCourse
from Models.Users.Student import Student
import django.db.models as models

class Students_DegreeCourses(CustomModel):
    StudentId = models.ForeignKey(to=Student, to_field=Student.StudentId)
    DegreeCourseId = models.ForeignKey(to=DegreeCourse, to_field=DegreeCourse.DegreeCourseId)
    CurrentSemester = models.IntegerField(null=False, default=0)
    CountOfSemesteres = models.IntegerField(null=False, default=0)
