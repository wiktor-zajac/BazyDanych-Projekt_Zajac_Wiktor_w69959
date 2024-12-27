from django.db.models.enums import IntegerChoices


class PassOrNotGrades(IntegerChoices):
    PASSED = 0
    NOT_PASSED = 1
