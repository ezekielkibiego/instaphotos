# Generated by Django 2.2 on 2021-12-03 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]