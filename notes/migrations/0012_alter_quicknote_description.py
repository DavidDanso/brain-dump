# Generated by Django 4.0 on 2023-03-02 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0011_alter_quicknote_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quicknote',
            name='description',
            field=models.TextField(blank=True, max_length=1255, null=True),
        ),
    ]
