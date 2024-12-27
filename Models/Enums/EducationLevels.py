from django.db.models.enums import IntegerChoices


class EducationLevels(IntegerChoices):
    NONE = 0
    BACHELOR = 1
    ENGINEER = 2
    MASTER = 3
    DOCTOR = 4
    PROFESSOR = 5
