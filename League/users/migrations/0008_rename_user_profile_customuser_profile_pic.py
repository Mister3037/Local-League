# Generated by Django 5.0.6 on 2024-05-27 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='user_profile',
            new_name='profile_pic',
        ),
    ]
