# Generated by Django 4.2.4 on 2023-08-13 15:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="contact",
            old_name="datatime",
            new_name="date",
        ),
        migrations.AlterField(
            model_name="contact",
            name="desc",
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name="contact",
            name="phone",
            field=models.IntegerField(),
        ),
    ]
