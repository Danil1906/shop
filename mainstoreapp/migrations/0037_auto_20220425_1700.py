# Generated by Django 3.2.9 on 2022-04-25 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainstoreapp', '0036_auto_20220123_1418'),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='#', help_text='Ссылка которая при клике будет куда то уводить пользователя', max_length=250, verbose_name='Описание')),
                ('is_published', models.BooleanField(default=False, help_text='добавить/снять с публикации в слайдере', verbose_name='Публикация')),
                ('photo', models.ImageField(blank=True, help_text='Для большого слайдера размер 966*400 (цвет фона страницы #f3efef) \n    . Для маленького банера размер 272*400. Для лучшего обображения в слайдере следует собирать картинки указанных рамзмеров.', upload_to='backgrounds/%Y/%m/%d/')),
                ('type_post', models.CharField(choices=[('UNDER_HEAD', 'Сразу под шапкой (до 3х постов)'), ('IN_HEAD', 'Между логотипом и поиском на в шапке (лишь 1 пост)')], default='SLIDER', max_length=25, verbose_name='Где расположить объявление')),
            ],
            options={
                'verbose_name': 'Баннер',
                'verbose_name_plural': 'Баннеров/ы',
            },
        ),
        migrations.AlterField(
            model_name='category',
            name='photo',
            field=models.ImageField(blank=True, default='default.webp', upload_to='photos_category/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, default='default_prod_black.webp', upload_to='photos/%Y/%m/%d/'),
        ),
    ]