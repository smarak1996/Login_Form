from django.db import models

class LoginData(models.Model):
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    
