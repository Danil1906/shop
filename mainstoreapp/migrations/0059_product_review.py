# Generated by Django 3.2.9 on 2022-05-01 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainstoreapp', '0058_alter_profile_purchased'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='review',
            field=models.JSONField(default={}, verbose_name='Отзывы на товар'),
        ),
    ]