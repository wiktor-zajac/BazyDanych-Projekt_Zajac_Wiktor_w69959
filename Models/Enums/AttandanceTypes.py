from django.db.models.enums import IntegerChoices


class AttandanceTypes(IntegerChoices):
    ABSENT = 0
    PRESENT = 1
    LATE = 2
    EXEMPT = 3
    EXCUSED = 4
