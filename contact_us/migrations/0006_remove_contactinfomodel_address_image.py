# Generated by Django 2.2.27 on 2022-02-27 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0005_auto_20220227_1206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactinfomodel',
            name='address_image',
        ),
    ]
