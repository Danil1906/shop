# Generated by Django 3.2.9 on 2021-12-20 15:55

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('mainstoreapp', '0012_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None),
        ),
    ]
