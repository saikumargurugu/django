from django.db import models

class det(models.Model):
    name= models.CharField(max_length=100 )
    email= models.CharField(max_length=100)
    phno= models.CharField(max_length=100)

def __str__(self):
    return self
class Meta:
     unique_together = (("email", "phno"),)