# Generated by Django 3.2.9 on 2021-11-12 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, help_text='Опишите товар', verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=6, verbose_name='Цена')),
                ('date_published', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('available', models.BooleanField(default=False, verbose_name='Наличие')),
            ],
        ),
    ]
