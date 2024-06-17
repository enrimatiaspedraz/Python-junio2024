from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200)
    
class Task(models.Model):    
    producto = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE )
  
    done = models.BooleanField(default=False)
    
    