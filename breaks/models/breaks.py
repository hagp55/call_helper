from django.db import models

from django.contrib.auth import get_user_model

from breaks.constants import (
    BREAK_CREATED_DEFAULT,
    BREAK_CREATED_STATUS,
)
from breaks.models.dicts import BreakStatus

USER = get_user_model()


class Break(models.Model):
    replacement = models.ForeignKey(
        to="breaks.Replacement",
        on_delete=models.CASCADE,
        related_name="breaks",
        verbose_name="Смена",
    )
    employee = models.ForeignKey(
        USER,
        on_delete=models.CASCADE,
        related_name="breaks",
        verbose_name="Сотрудник",
        blank=True,
    )

    break_start = models.TimeField("Начало обеда", null=True, blank=True)
    break_end = models.TimeField("Конец обеда", null=True, blank=True)
    status = models.ForeignKey(
        "breaks.BreakStatus",
        on_delete=models.RESTRICT,
        related_name="breaks",
        verbose_name="Статус",
        blank=True,
    )

    class Meta:
        verbose_name = "Обеденный перервыв"
        verbose_name_plural = "Обеденные перерывы"
        ordering = ("-replacement__date", "break_start")

    def save(self, *args, **kwargs) -> None:
        if not self.pk:
            status, created = BreakStatus.objects.get_or_create(
                code=BREAK_CREATED_STATUS,
                defaults=BREAK_CREATED_DEFAULT,
            )
            self.status = status
            # self.status = BreakStatus.objects.filter(code=BREAK_CREATED_STATUS).first()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"Обед пользователя {self.employee} ({self.pk})"
