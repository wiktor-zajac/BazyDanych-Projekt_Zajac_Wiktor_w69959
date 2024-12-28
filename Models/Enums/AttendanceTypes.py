from django.db.models.enums import IntegerChoices


class AttendanceTypes(IntegerChoices):
    UNKNOWN = 0
    ABSENT = 1
    PRESENT = 2
    LATE = 3
    EXEMPT = 4
    EXCUSED = 5
