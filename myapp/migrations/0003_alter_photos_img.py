# Generated by Django 3.2.5 on 2021-08-01 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_photos_disc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='img',
            field=models.CharField(max_length=300),
        ),
    ]
