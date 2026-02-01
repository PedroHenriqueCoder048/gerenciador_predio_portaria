from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import AbstractUser

EMPLOYEE_ROLE_CHOICES = [
    ('cleaning', 'Limpeza'),
    ('doorman', 'Porteiro'),
    ('caretaker', 'Zelador'),
    ('electrician', 'Eletricista'),
    ('plumber', 'Encanador'),
    ('security', 'Segurança'),
    ('gardener', 'Jardineiro'),
    ('maintenance', 'Manutenção Geral'),
]


class Passon(AbstractUser):
    cpf = models.CharField(unique=True,max_length=11)
    username = models.CharField(max_length=150, unique=True, blank=True, null=True)
    
    email = models.EmailField(unique=True)

    class Meta:
        ordering = ['cpf']

class CustomUser(Passon):
    
    gate_password = models.CharField(
        max_length=6,
        validators=[MinLengthValidator(6)],
        null=True)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = [] 

class Residente(CustomUser):

    house_number = models.IntegerField(unique=True,validators=[MinLengthValidator(1)])

    floor_number = models.IntegerField(validators=[MinLengthValidator(1)])

    class Meta:
        verbose_name = "Moradores"
        verbose_name_plural = "Moradores"

class Employee(CustomUser):
    department = models.CharField(choices=EMPLOYEE_ROLE_CHOICES)


    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"