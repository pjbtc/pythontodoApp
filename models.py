# tasks/models.py
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)  # Title of the task
    completed = models.BooleanField(default=False)  # Whether the task is completed

    def __str__(self):
        return self.title

