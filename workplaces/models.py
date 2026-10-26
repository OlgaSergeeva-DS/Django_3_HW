from django.conf import settings
from django.db import models


# Create your models here.
class Workplace(models.Model):
    """Модель рабочего места."""

    desk_number = models.CharField(
        max_length=20,
        unique=True,  # Номера столов не должны повторяться
        verbose_name="Номер стола",
    )
    description = models.TextField(
        verbose_name="Дополнительная информация",
        blank=True,
        help_text="Например: 'У окна', 'Рядом с принтером'",
    )
    # Связь "один к одному" с моделью пользователя (сотрудника)
    employee = models.OneToOneField(
        settings.AUTH_USER_MODEL,  # Ссылаемся на нашу кастомную модель
        on_delete=models.SET_NULL,  # Если сотрудника удалят, рабочее место останется, но станет свободным
        null=True,
        blank=True,
        verbose_name="Закреплённый сотрудник",
        related_name="workplace",  # Позволит из сотрудника получить его рабочее место: user.workplace
    )

    class Meta:
        verbose_name = "Рабочее место"
        verbose_name_plural = "Рабочие места"

    def __str__(self):
        return f"Стол №{self.desk_number}"
