from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your tests here. this is where I would put my own fields
class CustomUser(AbstractUser):

    def _str_(self):
        return self.username



