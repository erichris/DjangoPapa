# Generated by Django 2.0.7 on 2018-10-31 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0010_auto_20181031_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='phone',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]