# Generated by Django 3.2.9 on 2022-04-26 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainstoreapp', '0040_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=250, verbose_name='электронная почта'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(help_text='Ссылка которая при клике будет куда то уводить пользователя', max_length=250, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.CharField(help_text='Ссылка которая при клике будет куда то уводить пользователя', max_length=250, verbose_name='Описание'),
        ),
    ]
