# Generated by Django 2.2.27 on 2022-02-13 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_sharing', '0009_delete_seosocialsharedatamodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imageauxdatamodel',
            name='alt',
        ),
    ]
