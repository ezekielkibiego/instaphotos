# Generated by Django 3.2.7 on 2021-12-04 20:40

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('instaapp', '0007_profiles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='posts',
            field=tinymce.models.HTMLField(),
        ),
    ]
