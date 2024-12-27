from django.db.models.enums import IntegerChoices


class GradeTypes(IntegerChoices):
    PassOrNot = 0
    RegularGrade = 1
