# Generated by Django 3.2.7 on 2021-12-06 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaapp', '0015_auto_20211206_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=80, null=True),
        ),
    ]