from django.db import models

class Item(models.Model):
    name_item = models.TextField(verbose_name='Название вещи', max_length=200)
    price_item = models.FloatField(verbose_name='Стоимость вещи', max_length=10)
    url_icon = models.TextField(verbose_name='Ссылка на изображение', max_length=999, default= ' ')

    def __str__(self):
        return '%s %s' % (self.name_item, self.price_item)

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

