# Generated by Django 2.2.7 on 2019-12-13 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20191213_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price_item',
            field=models.FloatField(null=True, verbose_name='Стоимость вещи'),
        ),
    ]