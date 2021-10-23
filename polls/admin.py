from django.contrib import admin
from .models import Question, Choice

# Register your models here.


# new decorator way
@admin.register(Question, Choice)
class PollsAdmin(admin.ModelAdmin):
    pass
