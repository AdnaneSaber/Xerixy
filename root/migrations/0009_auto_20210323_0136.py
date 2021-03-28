# Generated by Django 3.1.7 on 2021-03-23 00:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0008_auto_20210323_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leads',
            name='phone',
            field=models.CharField(max_length=64, validators=[django.core.validators.RegexValidator(message='Please enter a valid phone number like : (0123456789 or +1234567890)', regex='^\\s*(?:\\+?(\\d{1,3}))?[-. (]*(\\d{3})[-. )]*(\\d{3})[-. ]*(\\d{4})(?: *x(\\d+))?\\s*$')]),
        ),
    ]
