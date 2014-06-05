from django.db import models
from django.contrib.auth.models import User

def get_upload_file_name(instance,filename):
    return '%s' % filename

class Course(models.Model):
    course_name=models.CharField(max_length=20)

class Task(models.Model):
    task_name=models.CharField(max_length=30)
    course = models.ForeignKey(Course) 
    
class TaskFile(models.Model):
    file_object = models.FileField(upload_to=get_upload_file_name)
    task = models.ForeignKey(Task)

class University(models.Model):
    university_name = models.CharField(max_length=30)
    
class Student(models.Model):

    OCCUPATION_CHOICE=(
        ('no',''),
        ('st','student'),
        ('em','employed'),
        ('se','self employed'),
    )
    
    
    occupation = models.CharField(max_length=20, choices=OCCUPATION_CHOICE)
    #course = models.ForeignKey(Course)
    phone_number = models.IntegerField()
    age = models.IntegerField()
    user = models.OneToOneField(User)

class Tutor(models.Model):
    
    course = models.ForeignKey(Course)
    user = models.OneToOneField(User)
    
# Create your models here.
