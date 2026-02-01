from django.db import models
from django.core.validators import MinLengthValidator

class Vehicle(models.Model):
    plate  = models.CharField(
    max_length=7,
    validators=[MinLengthValidator(7)])

