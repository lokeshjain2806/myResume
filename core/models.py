from django.db import models


# Create your models here.
class Con(models.Model):
    name = models.CharField(max_length=70, null=True)
    email = models.EmailField(max_length=70, null=True)
    subject = models.CharField(max_length=250, null=True)
    message = models.TextField(max_length=1500, null=True)
