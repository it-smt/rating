from django.db import models


class Rank(models.Model):
    """Модель звания."""

    class RankChoices(models.TextChoices):
        """Виды званий."""

        BRONZE = "Бронза", "Бронза"
        SILVER = "Серебро", "Серебро"
        GOLD = "Золото", "Золото"
        DIAMOND = "Алмаз", "Алмаз"
        JEDI = "Джедай", "Джедай"

    image = models.FileField(
        verbose_name="Изображение", upload_to="rank/images/", blank=True, null=True
    )
    title = models.CharField(
        verbose_name="Название",
        max_length=7,
        choices=RankChoices.choices,
        default=RankChoices.BRONZE.value,
    )
    prize = models.PositiveIntegerField(verbose_name="Приз", default=0)
    orders_count = models.PositiveIntegerField(
        verbose_name="Количество заказов", default=0
    )

    class Meta:
        verbose_name = "Звание"
        verbose_name_plural = "Звания"
        ordering = ["prize"]

    def __str__(self) -> str:
        return f"{self.title} - {self.prize} ₽"


class People(models.Model):
    """Модель человека в рейтинге."""

    class GradeChoices(models.TextChoices):
        """Грейд."""

        UP = "up", "up"
        REMAIN = "remain", "remain"
        DOWN = "down", "down"

    name = models.CharField(verbose_name="Имя", max_length=100, blank=True, null=True)
    call_sign = models.CharField(max_length=100, unique=True)
    orders_count = models.IntegerField(default=0)
    rank = models.ForeignKey(
        Rank,
        verbose_name="Звание",
        on_delete=models.PROTECT,
        related_name="peoples",
        blank=True,
        null=True,
    )
    grade = models.CharField(
        verbose_name="Грейд",
        max_length=7,
        choices=GradeChoices.choices,
        default=GradeChoices.REMAIN.value,
    )

    class Meta:
        verbose_name = "Человек"
        verbose_name_plural = "Люди"
        ordering = ["-orders_count"]

    def __str__(self) -> str:
        return f"{self.name}({self.call_sign}) - {self.rank}({self.grade})"
