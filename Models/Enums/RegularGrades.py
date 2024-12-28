from django.db.models.enums import IntegerChoices


class RegularGrades(IntegerChoices):
    TWO_ZERO = 20
    THREE_ZERO = 30
    THREE_HALF = 35
    FOUR_ZERO = 40
    FOUR_HALF = 45
    FIVE_ZERO = 50
