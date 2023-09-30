from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from .managers import UserManager
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=50)
    email = models.EmailField(unique=True, max_length=254)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    mobile_number= models.CharField(max_length=10,blank=True)
    designation = models.CharField(max_length=20, default="")
    department = models.CharField(max_length=20, default="")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'designation','department','mobile_number']

    objects = UserManager()

    def __str__(self):
        return self.username

class Employee(models.Model):
    employee_CPF = models.IntegerField(unique=True)
    employee_First_name = models.CharField(max_length=20)
    employee_Last_name = models.CharField(max_length=20)
    employee_Dept = models.CharField(max_length=20)
    employee_Designation = models.CharField(max_length=50)
    employee_Email = models.EmailField(max_length=50,unique=True)
    employee_HoD = models.BooleanField(default=False)
    employee_Mob = models.IntegerField(unique=True)

    # To control the default ordering of records
    class Meta:
        ordering = []
    
    # Represent the record.
    def __str__(self):
        return f'{self.employee_First_name} {self.employee_Last_name} - {self.employee_Designation}({self.employee_Dept})'