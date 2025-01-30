from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class StatusModel(models.Model):
    status = models.CharField(max_length=100)
    def __str(self):
        return self.status 

class PriorityModel(models.Model):
    priority = models.CharField(max_length=100)
    def __str(self):
        return self.priority 

class TaskBoard(models.Model):
    taskname = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.ForeignKey(StatusModel,on_delete=models.PROTECT)
    priority = models.ForeignKey(PriorityModel,on_delete=models.PROTECT)
    progress = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.taskname
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.CharField(max_length=10000)
