# Generated by Django 3.2.9 on 2022-01-14 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainstoreapp', '0031_alter_promocode_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='photo',
            field=models.ImageField(blank=True, default='default.png', upload_to='photos_category/%Y/%m/%d/'),
        ),
    ]
