# Generated by Django 2.2.10 on 2020-05-29 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_coupon_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='amount',
            field=models.FloatField(default=20),
        ),
    ]
