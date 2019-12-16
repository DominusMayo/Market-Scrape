# Generated by Django 2.2.7 on 2019-11-20 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='comment_count',
            field=models.IntegerField(default=0, verbose_name='Количество комментариев'),
        ),
        migrations.AlterField(
            model_name='item',
            name='count_item_buy',
            field=models.IntegerField(default=0, verbose_name='Количество покупок'),
        ),
    ]