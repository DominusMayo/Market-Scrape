from django.db import models

class Item(models.Model):
    name_item = models.TextField(verbose_name='Название вещи', max_length=200, db_index=True)
    price_item = models.FloatField(verbose_name='Стоимость вещи', max_length=10, db_index=True)
    url_icon = models.CharField(verbose_name='Ссылка на изображение', max_length=999, default= ' ', db_index=True)

    def __str__(self):
        return '%s %s' % (self.name_item, self.price_item)

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

