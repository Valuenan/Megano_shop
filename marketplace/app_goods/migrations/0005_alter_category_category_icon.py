# Generated by Django 3.2.13 on 2022-09-01 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_goods', '0004_auto_20220825_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_icon',
            field=models.FileField(default='C:\\Users\\Аня\\PycharmProjects\\python_django_group_diploma\\marketplace\\media\\icons\\categories\\test_category_icon.jpg', upload_to='icons/categories/', verbose_name='иконка категории'),
        ),
    ]