from django.db import models

from django.contrib.auth import get_user_model

USER = get_user_model()


class Replacement(models.Model):
    name = models.CharField("Название", max_length=255)
    group = models.ForeignKey(
        to="breaks.Group",
        on_delete=models.CASCADE,
        related_name="replacements",
        verbose_name="Группа",
    )
    date = models.DateField("Дата смены")
    break_start = models.TimeField("Начало обеда")
    break_end = models.TimeField("Конец обеда")
    break_max_duration = models.PositiveSmallIntegerField(
        "Максимальная продолжительность обеда"
    )

    class Meta:
        verbose_name = "Смену"
        verbose_name_plural = "Смены"
        ordering = ("-date",)

    def __str__(self) -> str:
        return f"Смена №{self.pk} для {self.group}"


class ReplacementEmployee(models.Model):
    replacement = models.ForeignKey(
        to="breaks.Replacement",
        on_delete=models.CASCADE,
        related_name="employees",
        verbose_name="Смена",
    )

    employee = models.ForeignKey(
        to=USER,
        on_delete=models.CASCADE,
        related_name="replacements",
        verbose_name="Сотрудник",
    )

    status = models.ForeignKey(
        to="breaks.ReplacementStatus",
        on_delete=models.CASCADE,
        related_name="replacement_employees",
        verbose_name="Статус",
    )

    class Meta:
        verbose_name = "Смену - Работник"
        verbose_name_plural = "Смены - Работники"
        ordering = ("-status",)

    def __str__(self) -> str:
        return f"Смена №{self.replacement} для {self.employee}"
