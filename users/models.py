from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    DEPARTMENT = (
        ('ICT', 'ICT'),
        ('Accounting', 'Accounting'),
        ('Human Resource', 'Human Resource'),
        ('Legal', 'Legal'),
    )
    POSITION = (
        ('Manager', 'Manager'),
        ('Driver', 'Driver'),
        ('Clerk', 'Clerk'),
        ('Receptionist', 'Receptionist')
    )
    MARITAL_STATUS_LIST = (
        ('Single', 'Single'),
        ('Divorced', 'Divorced'),
        ('Married', 'Married'),
        ('Widowed', 'Widowed'),
    )
    WORK_TYPE = (
        ('Part Time', 'Part Time'),
        ('Full Time', 'Full Time')
    )
    WORK_STATUS = (
        ('Vacation', 'On Vacation'),
        ('Active', 'Active'),
        ('Retired', 'Retired')
    )
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('male', 'male'), ('female', 'female')], null=True, blank=True)
    dob = models.DateField(verbose_name='date of birth', null=True, blank=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    phone = models.CharField(max_length=14, unique=True, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    avatar = models.ImageField(upload_to='passports', null=True, blank=True)
    position = models.CharField(max_length=255, choices=POSITION, null=True, blank=True)
    marital_status = models.CharField(max_length=50, choices=MARITAL_STATUS_LIST, default='Single', null=True, blank=True)
    work_status = models.CharField(max_length=20, choices=WORK_STATUS, default='Active', null=True, blank=True)
    date_employed = models.DateField(null=True, blank=True)
    work_type = models.CharField(max_length=20, choices=WORK_TYPE, default='Full', null=True, blank=True)
    bio = models.TextField(max_length=500, null=True, blank=True)
    department = models.CharField(max_length=100, choices=DEPARTMENT, null=True, blank=True)

    def __str__(self):
        return self.email

    def fullname(self):
        if self.first_name and self.last_name:
            return self.first_name + ' ' + self.last_name
        else:
            return self.username
