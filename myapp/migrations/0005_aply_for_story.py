# Generated by Django 3.2.5 on 2021-08-04 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_photos_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='aply_for_story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('write', models.TextField(default='')),
            ],
        ),
    ]