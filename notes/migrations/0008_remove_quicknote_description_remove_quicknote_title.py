# Generated by Django 4.0 on 2023-03-01 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0007_quicknote_description_quicknote_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quicknote',
            name='description',
        ),
        migrations.RemoveField(
            model_name='quicknote',
            name='title',
        ),
    ]
