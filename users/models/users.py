from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

from users.managers import CustomUserManager
from .profile import Profile


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


@receiver(post_save, sender=User)
def post_save_user(sender, instance, created, **kwargs):
    if not hasattr(instance, "profile"):
        Profile.objects.create(user=instance)
