# Generated by Django 2.0.7 on 2018-10-31 20:04

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0009_auto_20181031_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, max_length=31),
        ),
    ]
