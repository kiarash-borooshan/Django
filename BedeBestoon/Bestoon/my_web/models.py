from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Expense(models.Model):
    Title = models.CharField(max_length=255)
    Amount = models.BigIntegerField()
    Date = models.DateTimeField()
    My_User = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="My_User"
    )

    Choice = (
        ("draft", "Draft"),
        ("publish", "Publish")
    )
    Choose = models.CharField(
        max_length=250,
        choices=Choice,
        default="draft"
    )

    def __str__(self):
        return f"{self.Title}: {self.Amount}"
