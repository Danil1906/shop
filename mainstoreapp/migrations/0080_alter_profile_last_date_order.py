# Generated by Django 3.2.9 on 2022-05-09 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainstoreapp', '0079_auto_20220509_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='last_date_order',
            field=models.DateTimeField(default=None, null=True, verbose_name='Дата последнего заказа'),
        ),
    ]
