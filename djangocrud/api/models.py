from django.db import models

class Movie(models.Model):
    title=models.CharField(max_length=20)
    desc=models.CharField(max_length=20)
    year=models.IntegerField()
    
