# Generated by Django 3.1.7 on 2021-09-08 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0020_auto_20210908_2111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='Theme',
        ),
    ]
