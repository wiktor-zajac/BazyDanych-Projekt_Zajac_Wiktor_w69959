from django.utils import timezone
from Models.CustomModel import CustomModel 
from Models.Courses.Course import Course
from Models.Enums.AttendanceTypes import AttendanceTypes
from Models.Users.Profesor import Profesor
from Models.Users.Student import Student
import django.db.models as models


class CourseAttendance(CustomModel):
    CourseAttendanceId = models.BigAutoField(primary_key=True)
    StudentId = models.ForeignKey(Student, to_field=Student.StudentId)
    CourseId = models.ForeignKey(Course, to_field=Course.CourseId)
    ProfesorId = models.ForeignKey(Profesor, to_field=Profesor.ProfesorId)
    DateTime = models.DateTimeField(default=timezone.now)
    Status = models.IntegerField(choices=AttendanceTypes, default=AttendanceTypes.UNKNOWN)
