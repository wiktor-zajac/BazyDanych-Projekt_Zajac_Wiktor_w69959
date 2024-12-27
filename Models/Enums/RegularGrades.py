from django.db.models.enums import IntegerChoices


class RegularGrades(IntegerChoices):
    TWO_ZERO = 0
    THREE_ZERO = 1
    THREE_HALF = 2
    FOUR_ZERO = 3
    FOUR_HALF = 4
    FIVE_ZERO = 5
