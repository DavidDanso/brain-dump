# Generated by Django 4.0 on 2023-03-03 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('folders', '0007_foldername_number_of_notes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FolderNote',
            new_name='Note',
        ),
    ]
