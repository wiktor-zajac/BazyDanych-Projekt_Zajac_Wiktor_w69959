from django.db.models.enums import IntegerChoices


class GradeTypes(IntegerChoices):
    PassOrNotGrade = 0
    RegularGrade = 1
