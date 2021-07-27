from django.db import models

class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=100)
    esal = models.FloatField()
    eaddr = models.TextField()
    owner = models.ForeignKey('auth.User',related_name='employee',on_delete=models.CASCADE)
    

