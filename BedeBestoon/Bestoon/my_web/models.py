from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    Status_Choices = (
        ("draft", "Draft"),
        ("publish", "Publish")
    )
    Title = models.CharField(
        max_length=200
    )
    Slug = models.SlugField(
        max_length=250,
        unique_for_date="publish"
    )
    Author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="blog_post"
    )
    Body = models.TextField()
    publish = models.DateTimeField(
        default=timezone.now
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    update = models.DateTimeField(
        auto_now=True
    )
    Status = models.CharField(
        max_length=10,
        choices=Status_Choices,
        default="draft"
    )

    # class Meta:
    #     ordering = "-publish"

    def __str__(self):
        return self.Title


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
