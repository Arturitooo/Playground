from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    task = models.CharField(max_length=150)
    date = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.task
