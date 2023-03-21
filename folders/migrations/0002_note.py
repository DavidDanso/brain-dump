# Generated by Django 4.0 on 2023-03-03 12:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('folders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, max_length=100000, null=True)),
                ('updated_time_stamp', models.DateTimeField(auto_now=True)),
                ('created_time_stamp', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'ordering': ['-updated_time_stamp'],
            },
        ),
    ]
