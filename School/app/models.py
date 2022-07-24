from django.db import models
from django.contrib.auth.models import User
class Principle(models.Model):
    name=models.CharField(max_length=20)


    def __str__(self):
        return self.name

class Teacher(models.Model):
    student_name=models.CharField(max_length=30)
    subject=models.CharField(max_length=30)
    marks=models.FloatField()

    def __str__(self):
        return self.student_name



class Student(models.Model):
    subject=models.CharField(max_length=30)

    def __str__(self):
        return self.subject
