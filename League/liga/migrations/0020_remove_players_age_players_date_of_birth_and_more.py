# Generated by Django 5.0.6 on 2024-05-27 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liga', '0019_alter_teamtable_drawn_alter_teamtable_gd_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='players',
            name='age',
        ),
        migrations.AddField(
            model_name='players',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='players',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='player/'),
        ),
    ]