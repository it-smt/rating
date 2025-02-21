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

    title = models.CharField(
        verbose_name="Название",
        max_length=7,
        choices=RankChoices.choices,
        default=RankChoices.BRONZE.value,
    )

    class Meta:
        verbose_name = "Звание"
        verbose_name_plural = "Звания"

    def __str__(self) -> str:
        return self.title


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

    def __str__(self) -> str:
        return f"{self.name}({self.call_sign}) - {self.rank}({self.grade})"
