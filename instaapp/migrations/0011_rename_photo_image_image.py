# Generated by Django 3.2.7 on 2021-12-05 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instaapp', '0010_auto_20211205_1745'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='photo',
            new_name='image',
        ),
    ]
