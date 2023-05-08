# Generated by Django 3.2.3 on 2023-05-08 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pilot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('callsign', models.CharField(max_length=50)),
                ('gunnery', models.IntegerField(blank=True, default=4)),
                ('piloting', models.IntegerField(blank=True, default=5)),
                ('experience', models.IntegerField(blank=True, default=5)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('status', models.IntegerField(choices=[(0, 'Not Available'), (1, 'Available')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Mech',
            fields=[
                ('pilots', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='mechs', serialize=False, to='webapp.pilot')),
                ('name', models.CharField(max_length=50)),
                ('category', models.IntegerField(choices=[(0, 'Light'), (1, 'Medium'), (2, 'Heavy'), (3, 'Assault')], default=0)),
                ('weight', models.IntegerField(choices=[(0, '20 Ton'), (1, '25 Ton'), (2, '30 Ton'), (3, '35 Ton'), (4, '40 Ton'), (5, '45 Ton'), (6, '50 Ton'), (7, '55 Ton'), (8, '60 Ton'), (9, '65 Ton'), (10, '70 Ton'), (11, '75 Ton'), (12, '80 Ton'), (13, '85 Ton'), (14, '90 Ton'), (15, '95 Ton'), (16, '100 Ton')], default=0)),
                ('tech_level', models.IntegerField(choices=[(0, 'Inner Sphere'), (1, 'Clan'), (2, 'Prototype')], default=0)),
                ('role', models.IntegerField(choices=[(0, 'Ambusher'), (1, 'Brawler'), (2, 'Juggernaut'), (3, 'Missle Boat'), (4, 'Scout'), (5, 'Skirmisher'), (6, 'Sniper'), (7, 'Striker')], default=0)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('stock', models.IntegerField(default=2)),
                ('description', models.TextField(blank=True)),
                ('record_sheet', models.URLField()),
                ('battle_value', models.IntegerField(default=9999)),
                ('status', models.IntegerField(choices=[(0, 'Not Available'), (1, 'Available')], default=0)),
            ],
        ),
    ]
