# Generated by Django 3.2.9 on 2022-04-26 23:13

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('mainstoreapp', '0041_auto_20220426_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='fio',
            field=models.CharField(blank=True, max_length=250, verbose_name='Ф.И.О.'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None, verbose_name='номер телефона'),
        ),
    ]