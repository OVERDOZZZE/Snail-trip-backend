# Generated by Django 4.1.7 on 2023-03-17 14:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tour", "0009_alter_tour_qr_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tour",
            name="qr_code",
            field=models.CharField(blank=True, default="", max_length=8, null=True),
        ),
    ]
