from datetime import datetime

from django.db import models

from users.models import User

NULLABLE = {
    'null': True,
    'blank': True
}


class Habit(models.Model):
    """ класс описывает Атомные привычки """

    TITLE_PERIODICITY = [
        (1, 'каждый день'),
        (2, 'раз в два дня'),
        (3, 'раз в три дня'),
        (4, 'раз в четыре дня'),
        (5, 'раз в пять дней'),
        (6, 'раз в шесть дней'),
        (7, 'раз в семь дней')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', related_name='habit')
    place = models.CharField(max_length=150, verbose_name='место')
    time = models.DateTimeField(default=datetime.now(), verbose_name='время')
    action = models.CharField(max_length=150, verbose_name='действие')
    is_pleasant_habit = models.BooleanField(default=False, verbose_name='приятная привычка', **NULLABLE)
    related_habit = models.ForeignKey('self', verbose_name='приятная привычка', on_delete=models.CASCADE, **NULLABLE)
    periodicity = models.PositiveSmallIntegerField(verbose_name='периодичность', default=1, choices=TITLE_PERIODICITY)
    reward = models.TextField(verbose_name='вознаграждение', **NULLABLE)
    lead_time = models.TimeField(verbose_name='время выполнения',  default="00:02")
    is_published = models.BooleanField(default=False, verbose_name='признак публичности')

    def __str__(self):
        return f"я буду {self.action} в {self.time} в {self.place}"

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'


