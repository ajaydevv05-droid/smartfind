
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    ROLE_CHOICES = [
        ('student', 'Student'),
        ('staff', 'Staff'),
        ('college_admin', 'College Admin'),
    ]

    email = models.EmailField(unique=True)

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='student'
    )

    is_email_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username
