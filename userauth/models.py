from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add any additional user fields here
    pass
