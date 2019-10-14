from django.db import models

# Create your models here.

class AddStudent(models.Model):
    roll = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=10)
    dob = models.DateField()
    department = models.CharField(max_length=20)
    semester = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class AddHall(models.Model):
    hall = models.CharField(max_length=50)
    block = models.CharField(max_length=50)
    floor = models.CharField(max_length=50)
    capacity = models.IntegerField(default=0)
    def __str__(self):
        return self.hall


class Allocate(models.Model):
    roll = models.CharField(max_length=20, default="0")
    seatno =  models.CharField(max_length=10)
    student = models.ForeignKey(AddStudent, on_delete=models.CASCADE)
    hall = models.ForeignKey(AddHall, on_delete=models.CASCADE)
    def __str__(self):
        return self.seatno



