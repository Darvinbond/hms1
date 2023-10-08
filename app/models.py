from django.db import models

# Create your models here.


class Hall(models.Model):
    hall_id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=200)
    capacity = models.IntegerField()
    number_of_rooms = models.IntegerField()
    number_in_room = models.CharField(max_length=20)


class Student(models.Model):
    stud_id = models.IntegerField(primary_key=True, unique=True)
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=20)
    matric = models.CharField(max_length=20, default="")
    room_number = models.CharField(max_length=20)
    hallid = models.IntegerField(default=0)
    pending = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    password = models.TextField()


class Admin(models.Model):
    admin_id = models.IntegerField(primary_key=True, unique=True)
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.TextField()
    hallid = models.IntegerField()
