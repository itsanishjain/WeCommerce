# Generated by Django 2.1.5 on 2020-06-12 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='usertype',
        ),
    ]