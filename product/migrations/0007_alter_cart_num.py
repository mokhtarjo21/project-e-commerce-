# Generated by Django 4.0.4 on 2022-05-18 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_cart_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='num',
            field=models.DecimalField(decimal_places=0, max_digits=7),
        ),
    ]
