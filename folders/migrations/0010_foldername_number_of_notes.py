# Generated by Django 4.0 on 2023-03-03 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folders', '0009_remove_foldername_number_of_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='foldername',
            name='number_of_notes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
