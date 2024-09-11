import re
from datetime import date

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models

def validate_national_id(value:str):
    if len(value) != 10 or not value.isdigit():
        raise ValidationError('The national code must be 10 digits long and contain only numbers.')


def validate_mobile_number(value):
    if not re.match(r'^09\d{9}', value):
        raise ValidationError('Please enter a valid mobile number.')


class CustomUser(AbstractUser):
    national_id = models.CharField(max_length=10, validators=[validate_national_id], unique=True)
    mobile_number = models.CharField(max_length=11, validators=[validate_mobile_number], unique=True)
    birth_date = models.DateField(null=True)

    @property
    def age(self):
        if self.birth_date == None:
            return 0
        today = date.today()
        age = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age

    def __str__(self):
        return self.get_full_name()