# Generated by Django 5.0.3 on 2024-03-27 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ploshad', models.CharField(max_length=100, verbose_name='Площадь')),
                ('etazh', models.CharField(max_length=100, verbose_name='Этаж')),
                ('adres', models.CharField(max_length=100, verbose_name='Адрес')),
            ],
        ),
    ]
