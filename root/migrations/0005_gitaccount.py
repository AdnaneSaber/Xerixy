# Generated by Django 3.1.7 on 2021-05-15 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0004_maintenance'),
    ]

    operations = [
        migrations.CreateModel(
            name='gitAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=25)),
                ('repository', models.CharField(max_length=25)),
                ('upatePassword', models.CharField(max_length=50)),
            ],
        ),
    ]
