# Generated by Django 3.2.9 on 2022-05-06 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainstoreapp', '0066_auto_20220506_1809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordertext',
            name='email_server',
        ),
    ]
