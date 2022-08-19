# Generated by Django 3.2.13 on 2022-08-15 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_shops', '0003_auto_20220814_1516'),
        ('cart', '0002_rename_cartmodel_cartitems'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartitems',
            options={'ordering': ('added_at',), 'verbose_name': 'товар в корзине', 'verbose_name_plural': 'товары в корзине'},
        ),
        migrations.AddField(
            model_name='cartitems',
            name='shop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_shops.shop', verbose_name='id магазина'),
        ),
    ]
