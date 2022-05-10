# Generated by Django 3.2.9 on 2022-04-25 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainstoreapp', '0038_alter_sliderbanner_type_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sliderbanner',
            old_name='title',
            new_name='link',
        ),
        migrations.AlterField(
            model_name='sliderbanner',
            name='is_published',
            field=models.BooleanField(default=False, help_text='добавить/снять с публикации в слайдере. В случае слайдера, опубликовано может быть сразу несколько записей.\n                                       В случае фиксированного поста, публиковаться будет только 1, даже если отметка "Опубликовано" стоит на нескольких.', verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='sliderbanner',
            name='photo',
            field=models.ImageField(blank=True, help_text='Для большого слайдера размер 966*400 (цвет фона страницы #f3efef) \n    . Для маленького банера размер 272*400. Для лучшего отображения в слайдере следует собирать картинки указанных рамзмеров.', upload_to='backgrounds/%Y/%m/%d/'),
        ),
    ]