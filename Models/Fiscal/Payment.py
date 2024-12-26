from abc import ABC


class Payment(ABC):
    PaymentId: int
    Cost: str
    Paid: str
    Currency: str
    DueDate: int
    PaidDate: int
    Title: str
    StudentId: int
