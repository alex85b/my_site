# Generated by Django 4.1.7 on 2023-03-07 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_project_team_members_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='youtube_link',
            field=models.URLField(null=True),
        ),
    ]
