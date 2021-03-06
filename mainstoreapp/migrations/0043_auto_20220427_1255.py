# Generated by Django 3.2.9 on 2022-04-27 09:55

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('mainstoreapp', '0042_auto_20220427_0213'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='none', max_length=250, verbose_name='адрес'),
        ),
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.TextField(default='none', max_length=250, verbose_name='сообщение пользователю'),
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(default='none', max_length=250, verbose_name='электронная почта'),
        ),
        migrations.AddField(
            model_name='order',
            name='message_text',
            field=models.CharField(default='none', max_length=250, verbose_name='сообщение пользователю'),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None, verbose_name='номер телефона'),
        ),
        migrations.AddField(
            model_name='order',
            name='send',
            field=models.BooleanField(default=False, verbose_name='отправить сообщение пользователю'),
        ),
        migrations.AddField(
            model_name='order',
            name='send_has_done',
            field=models.BooleanField(default=False, verbose_name='сообщения были отправлены'),
        ),
        migrations.AddField(
            model_name='order',
            name='track_number',
            field=models.CharField(default='none', max_length=100, verbose_name='трек номер посылки'),
        ),
    ]
