# Generated by Django 5.0.6 on 2024-05-27 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liga', '0009_alter_team_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='image',
            new_name='images',
        ),
    ]
