from django.db import models

# Create your models here.

class Student(models.Model):
    std_id=models.IntegerField()
    std_name=models.CharField(max_length=40)
    std_email=models.EmailField(max_length=40)
    std_pass=models.CharField(max_length=10)
    comment=models.CharField(max_length=70,default="Not available")