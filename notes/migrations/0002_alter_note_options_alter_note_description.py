# Generated by Django 4.1.7 on 2023-03-03 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['-updated_time_stamp']},
        ),
        migrations.AlterField(
            model_name='note',
            name='description',
            field=models.TextField(blank=True, max_length=1255, null=True),
        ),
    ]
