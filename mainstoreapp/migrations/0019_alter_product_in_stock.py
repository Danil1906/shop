# Generated by Django 3.2.9 on 2021-12-21 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainstoreapp', '0018_alter_product_in_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='in_stock',
            field=models.BooleanField(default='Product.in_stock_method()', help_text='Это поле регулируется автоматически', verbose_name='В наличии'),
        ),
    ]