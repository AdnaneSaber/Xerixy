# Generated by Django 3.1.7 on 2021-06-12 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0016_auto_20210610_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='post_meta_description',
            field=models.CharField(blank=True, max_length=160),
        ),
        migrations.AddField(
            model_name='new',
            name='post_meta_title',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]
