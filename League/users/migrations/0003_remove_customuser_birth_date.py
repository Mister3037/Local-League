# Generated by Django 5.0.6 on 2024-05-27 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_birth_date_customuser_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='birth_date',
        ),
    ]
