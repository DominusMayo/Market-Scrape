from django.db import models

class Item(models.Model):
    name = models.CharField(verbose_name='Название вещи', max_length=400, db_index=True)
    price = models.FloatField(verbose_name='Стоимость вещи', max_length=10, db_index=True)
    url_icon = models.CharField(verbose_name='Ссылка на изображение', max_length=999, default= ' ', db_index=True)

    def __str__(self):
        return '%s %s' % (self.name, self.price)

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

