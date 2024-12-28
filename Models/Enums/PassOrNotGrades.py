from django.db.models.enums import IntegerChoices


class PassOrNotGrades(IntegerChoices):
    NOT_PASSED = 0
    PASSED = 1
