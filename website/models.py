from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from django.conf import settings

# Create your models here.

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    number = PhoneNumberField(blank=True)
    email = models.EmailField()
    content = models.TextField()

    def __str__(self):
        return f'Contact of {self.name}'
