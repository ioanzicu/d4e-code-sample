# Generated by Django 3.2.7 on 2021-10-16 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cat',
            old_name='name',
            new_name='nickname',
        ),
    ]
