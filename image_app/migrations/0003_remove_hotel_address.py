# Generated by Django 3.0.5 on 2020-04-22 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image_app', '0002_auto_20200422_1222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='address',
        ),
    ]