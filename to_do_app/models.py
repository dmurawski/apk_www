from django.db import models

# Create your models here.

class List(models.Model):
    list_name = models.CharField(max_length=200)
    dateCreate = models.DateTimeField("Stworzono")
    dateToFinish = models.DateTimeField("Deadline")

class Task(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    taskName = models.CharField(max_length=200)
    taskDescription = models.CharField(max_length=200)
    order = models.IntegerField(default=0)