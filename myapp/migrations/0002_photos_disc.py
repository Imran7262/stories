# Generated by Django 3.2.5 on 2021-07-27 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photos',
            name='disc',
            field=models.TextField(default=''),
        ),
    ]
