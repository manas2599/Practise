from django.db import models
from datetime import date
# Create your models here.


class studentdetails(models.Model):
    name = models.CharField(max_length=100)
    Father_Name = models.CharField(max_length=100)
    Mother_Name = models.CharField(max_length=100)
    Seat_Number = models.CharField(max_length=12)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=100)
    SEMESTER_CHOICES = [
        ('Semester 1', 'Semester 1'),
        ('Semester 2', 'Semester 2'),
        ('Semester 3', 'Semester 3'),
        ('Semester 4', 'Semester 4'),
        ('Semester 5', 'Semester 5'),
        ('Semester 6', 'Semester 6'),
        ('Semester 7', 'Semester 7'),
        ('Semester 8', 'Semester 8'),
    ]
    semester = models.CharField(max_length=15, default='Semester 1')
    date = models.DateField()

    def __str__(self):
        return self.name


class Courses(models.Model):
    course1 = models.CharField(max_length=100)
    course2 = models.CharField(max_length=100)
    course3 = models.CharField(max_length=100)
    course4 = models.CharField(max_length=100)
    course5 = models.CharField(max_length=100)
    course6 = models.CharField(max_length=100)
    SEMESTER_CHOICES = [
        ('Semester 1', 'Semester 1'),
        ('Semester 2', 'Semester 2'),
        ('Semester 3', 'Semester 3'),
        ('Semester 4', 'Semester 4'),
        ('Semester 5', 'Semester 5'),
        ('Semester 6', 'Semester 6'),
        ('Semester 7', 'Semester 7'),
        ('Semester 8', 'Semester 8'),
    ]
    semester = models.CharField(max_length=15, default='Semester 1')
    date = models.DateField()

    def __str__(self):
        return self.semester

class Assignment(models.Model):
    SEMESTER_CHOICES = [
        ('Semester 1', 'Semester 1'),
        ('Semester 2', 'Semester 2'),
        ('Semester 3', 'Semester 3'),
        ('Semester 4', 'Semester 4'),
        ('Semester 5', 'Semester 5'),
        ('Semester 6', 'Semester 6'),
        ('Semester 7', 'Semester 7'),
        ('Semester 8', 'Semester 8'),
    ]
    semester = models.CharField(max_length=15, default='Semester 1')        

    COURSE_CHOICES = [
        ('Course 1', 'Course 1'),
        ('Course 2', 'Course 2'),
        ('Course 3', 'Course 3'),
        ('Course 4', 'Course 4'),
        ('Course 5', 'Course 5'),
        ('Course 6', 'Course 6'),
    ]
    course = models.CharField(max_length=100, default='Course 1')        
    assignment = models.CharField(max_length=600, default='Assignment 1')
    date = models.DateField()

    def __str__(self):
        return self.assignment

class Marks(models.Model):
    name = models.CharField(max_length=100)
    SEMESTER_CHOICES = [
        ('Semester 1', 'Semester 1'),
        ('Semester 2', 'Semester 2'),
        ('Semester 3', 'Semester 3'),
        ('Semester 4', 'Semester 4'),
        ('Semester 5', 'Semester 5'),
        ('Semester 6', 'Semester 6'),
        ('Semester 7', 'Semester 7'),
        ('Semester 8', 'Semester 8'),
    ]
    semester = models.CharField(max_length=15, default='Semester 1')     
    course1 = models.CharField(max_length=500)
    mark1 = models.CharField(max_length=100)
    course2 = models.CharField(max_length=500)
    mark2 = models.CharField(max_length=100)
    course3 = models.CharField(max_length=500)
    mark3 = models.CharField(max_length=100)
    course4 = models.CharField(max_length=500)
    mark4 = models.CharField(max_length=100)
    course5 = models.CharField(max_length=500)
    mark5 = models.CharField(max_length=100)
    course6 = models.CharField(max_length=500)
    mark6 = models.CharField(max_length=100)
    date = models.DateField(default=date.today())

    def __str__(self):
        return self.name