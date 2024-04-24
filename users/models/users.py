from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

from users.models.managers import CustomUserManager


class User(AbstractUser):
    username = models.CharField(
        "Почта или телефон", max_length=150, unique=True, null=True, blank=True
    )
    email = models.EmailField("Электронная почта", unique=True, null=True, blank=True)
    phone_number = PhoneNumberField("Телефон", unique=True, null=True, blank=True)
    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    # REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.phone_number}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
