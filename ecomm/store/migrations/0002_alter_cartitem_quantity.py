# Generated by Django 4.2.5 on 2024-07-27 18:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cartitem",
            name="quantity",
            field=models.IntegerField(default=1),
        ),
    ]