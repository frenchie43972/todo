# Generated by Django 4.2.10 on 2024-02-16 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="task",
            name="priority",
        ),
    ]
