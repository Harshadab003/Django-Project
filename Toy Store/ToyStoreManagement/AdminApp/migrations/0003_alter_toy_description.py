# Generated by Django 4.2.3 on 2023-08-24 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0002_toy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toy',
            name='description',
            field=models.CharField(max_length=200),
        ),
    ]
