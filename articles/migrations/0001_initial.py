# Generated by Django 2.2.7 on 2019-11-20 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=300, verbose_name='Название статьи')),
                ('article_text', models.TextField(verbose_name='Текст статьи')),
                ('pub_date', models.DateTimeField(verbose_name='Дата публикации')),
                ('comment_count', models.IntegerField(verbose_name='Количество комментариев')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_item', models.CharField(max_length=200, verbose_name='Название вещи')),
                ('count_item_buy', models.IntegerField(verbose_name='Количество покупок')),
                ('price_item', models.FloatField(verbose_name='Цена вещи')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_author', models.CharField(max_length=200, verbose_name='Имя пользователя')),
                ('comment_text', models.TextField(verbose_name='Текст сообщения')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article')),
            ],
        ),
    ]