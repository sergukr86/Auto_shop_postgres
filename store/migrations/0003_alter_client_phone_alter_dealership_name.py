# Generated by Django 4.2.6 on 2023-10-25 21:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0002_rename_name_cartype_model_auto_alter_client_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="phone",
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name="dealership",
            name="name",
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
