# Generated by Django 5.0.6 on 2024-05-25 11:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liga', '0002_players_image_team_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('played', models.IntegerField()),
                ('won', models.IntegerField()),
                ('drawn', models.IntegerField()),
                ('lost', models.IntegerField()),
                ('gd', models.IntegerField()),
                ('points', models.IntegerField()),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='liga.team')),
            ],
        ),
    ]
