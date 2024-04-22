from django.db import models

from django.contrib.auth import get_user_model

USER = get_user_model()


class Organisation(models.Model):
    name = models.CharField("Название", max_length=255)
    director = models.ForeignKey(
        to=USER,
        on_delete=models.RESTRICT,
        related_name="organisation_director",
        verbose_name="Директор",
    )
    employees = models.ManyToManyField(
        USER,
        related_name="organisation_employees",
        verbose_name="Сотрудники",
        blank=True,
    )

    class Meta:
        verbose_name = "Огранизацию"
        verbose_name_plural = "Организации"
        ordering = ("name",)

    def __str__(self) -> str:
        return f"{self.name}"
