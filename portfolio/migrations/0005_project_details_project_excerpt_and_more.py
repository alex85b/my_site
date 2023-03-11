# Generated by Django 4.1.7 on 2023-03-11 17:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_alter_project_youtube_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='details',
            field=models.TextField(null=True, validators=[django.core.validators.MinLengthValidator(20)]),
        ),
        migrations.AddField(
            model_name='project',
            name='excerpt',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='youtube_link',
            field=models.URLField(null=True),
        ),
    ]
