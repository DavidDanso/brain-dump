# Generated by Django 4.0 on 2023-03-03 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('folders', '0003_rename_note_foldernote'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewFolder',
            new_name='FolderName',
        ),
    ]
