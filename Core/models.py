from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)


class Info(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="userrole")
    ROLE_CHOICES = (
        ('T', 'Teacher'),
        ('S', 'Student'),
    )
    role = models.CharField(max_length=1, choices=ROLE_CHOICES, default='S')
