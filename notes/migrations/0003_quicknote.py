# Generated by Django 4.1.7 on 2023-03-01 11:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_alter_note_options_alter_note_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuickNote',
            fields=[
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, max_length=1255, null=True)),
                ('updated_time_stamp', models.DateTimeField(auto_now=True)),
                ('created_time_stamp', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'ordering': ['-updated_time_stamp'],
            },
        ),
    ]
