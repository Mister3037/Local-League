# Generated by Django 5.0.6 on 2024-05-27 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liga', '0011_rename_images_team_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
