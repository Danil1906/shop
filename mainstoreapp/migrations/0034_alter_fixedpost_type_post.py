# Generated by Django 3.2.9 on 2022-01-15 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainstoreapp', '0033_auto_20220115_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixedpost',
            name='type_post',
            field=models.CharField(choices=[('UNDER_HEAD', 'Сразу под шапкой (до 3х постов)'), ('IN_HEAD', 'Между логотипом и поиском на в шапке (лишь 1 пост)')], default='UNDER_HEAD', max_length=25, verbose_name='Где распологается пост'),
        ),
    ]