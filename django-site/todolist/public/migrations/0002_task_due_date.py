# Generated by Django 5.1.1 on 2024-09-12 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("public", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="due_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
