# Generated by Django 4.0 on 2023-03-09 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_rename_full_name_profile_name'),
        ('folders', '0010_foldername_number_of_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='foldername',
            name='account_owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.profile'),
        ),
        migrations.AddField(
            model_name='note',
            name='account_owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.profile'),
        ),
    ]