# Generated by Django 5.0.6 on 2024-06-18 09:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("carrer", "0007_service_slug"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="service",
            name="slug",
        ),
    ]