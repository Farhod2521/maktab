from django.db import models
from django.contrib.postgres.fields import ArrayField

class GameLevel(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Bosqich nomi"
    )
    sentence = models.TextField(
        verbose_name="To‘g‘ri gap"
    )
    words = models.JSONField(
        verbose_name="Aralashtirilgan so‘zlar"
    )
    difficulty = models.CharField(
        max_length=20,
        choices=[('easy', 'Oson'), ('medium', 'O‘rtacha'), ('hard', 'Qiyin')],
        verbose_name="Qiyinchilik darajasi"
    )
    attempts = models.IntegerField(
        default=0,
        verbose_name="Urinishlar soni"
    )
    completed = models.BooleanField(
        default=False,
        verbose_name="Tugallanganmi"
    )
    stars = models.IntegerField(
        default=0,
        verbose_name="Yulduzlar soni"
    )

    class Meta:
        verbose_name = "O‘yin bosqichi"
        verbose_name_plural = "O‘yin bosqichlari"

    def __str__(self):
        return f"{self.id} - {self.name}"