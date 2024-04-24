from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        to="users.User",
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="profile",
        verbose_name="Пользователь",
    )
    telegram_id = models.CharField("Telegram ID", max_length=20, null=True, blank=True)

    class Meta:
        verbose_name = "Профиль пользователя"
        verbose_name_plural = "Профили пользователей"

    def __str__(self):
        return f"{self.user.username}"
