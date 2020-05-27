from django.db import models
from django.contrib.auth.models import AbstractUser


class Customer(AbstractUser):
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    # select_order = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.username)

