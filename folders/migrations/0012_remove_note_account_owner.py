# Generated by Django 4.0 on 2023-03-09 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('folders', '0011_foldername_account_owner_note_account_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='account_owner',
        ),
    ]
