from django.db import models

# Create your models here.

class TestUser(models.Model):
    name = models.CharField(max_length=100)


class Response(models.Model):
    name = models.ForeignKey(TestUser)
    question = models.PositiveIntegerField()
    answer = models.IntegerField()
    correct = models.NullBooleanField(null=True)
    
