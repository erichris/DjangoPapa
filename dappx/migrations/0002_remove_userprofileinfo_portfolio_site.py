# Generated by Django 2.1.2 on 2018-10-23 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='portfolio_site',
        ),
    ]