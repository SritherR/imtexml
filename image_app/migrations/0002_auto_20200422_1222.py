# Generated by Django 3.0.5 on 2020-04-22 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='address',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='hotel_Main_Img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
