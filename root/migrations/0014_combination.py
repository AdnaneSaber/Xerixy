# Generated by Django 3.1.7 on 2021-05-25 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0013_auto_20210516_0852'),
    ]

    operations = [
        migrations.CreateModel(
            name='Combination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.TextField()),
                ('prepositions', models.TextField()),
                ('locations', models.TextField()),
            ],
        ),
    ]
