# Generated by Django 4.1.7 on 2023-03-07 18:09

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('linkedin', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now=True)),
                ('github_link', models.URLField()),
                ('youtube_link', models.URLField()),
                ('description', models.TextField(validators=[django.core.validators.MinLengthValidator(20)])),
                ('slug', models.SlugField(unique=True)),
                ('skills', models.ManyToManyField(to='portfolio.skill')),
                ('team_lead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team', to='portfolio.team')),
                ('team_members', models.ManyToManyField(null=True, to='portfolio.team')),
            ],
        ),
    ]
