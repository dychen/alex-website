from django.db import models

# Create your models here.

class Response(models.Model):
    name = models.CharField(max_length=100)
    question = models.PositiveIntegerField()
    answer = models.IntegerField()
    correct = models.NullBooleanField(null=True)
    time = models.FloatField()
    
