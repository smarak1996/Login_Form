from django.db import models

class LoginData(models.Model):
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)


class SignUpData(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.BigIntegerField()
    password = models.CharField(max_length=100)
    
