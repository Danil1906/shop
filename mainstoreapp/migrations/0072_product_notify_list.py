# Generated by Django 3.2.9 on 2022-05-07 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainstoreapp', '0071_auto_20220506_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='notify_list',
            field=models.JSONField(default={}, help_text='Тут заносятся email пользователей, которых нужно уведомить о поступлении товара. Это просходит автоматически.', verbose_name='Список уведомлений'),
        ),
    ]
