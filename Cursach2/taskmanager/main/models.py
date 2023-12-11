from django.db import models


class Invest(models.Model):
    name = models.CharField('Название', max_length=30)
    old_price = models.IntegerField('Цена на данный момент в долларах')
    new_price = models.IntegerField('Ожидаемая цена в долларах')
    growth = models.FloatField('Ожидаемый рост в процентах')
    recommendations = models.TextField('Рекомендации по инвестициям')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Инвестиция'
        verbose_name_plural = 'Инвестиции'
