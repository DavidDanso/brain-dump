# Generated by Django 4.0 on 2023-03-15 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('folders', '0013_note_account_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='account_owner',
        ),
    ]
