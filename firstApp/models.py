from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
# Create your models here.

def validate_email(value):
    if not value.endswith('@gmail.com'):
        raise ValidationError(f"{value} is not a valid email address. Must be from gmail.com domain. ")

class Person(AbstractUser):
    email= models.EmailField(unique=True,validators=[validate_email])
    def __str__(self):
        return self.username
    

class Task(models.Model):
    STATUS_CHOICES=[
        ('TODO', 'To Do'),
        ('IN_PROGRESS', 'In progress'),
        ('DONE', 'Done'),
    ]
    title=models.CharField(max_length=200)
    description=models.TextField()
    due_date=models.DateField(null=True, blank=True)
    status=models.CharField(max_length=50,
                            default='ToDo', 
                            choices=STATUS_CHOICES)
    assigned_to=models.ForeignKey(Person, 
                                  on_delete=models.CASCADE, 
                                  related_name='tasks')


    def __str__(self):
        return self.title

