from django.contrib import admin
from .models import Expense, Post
# Register your models here.


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("Title", "Amount", "Date", "Choose")

@admin.register(Post)
class Post_Admin(admin.ModelAdmin):
    list_display = ("Title",)