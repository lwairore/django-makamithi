# Generated by Django 2.2.27 on 2022-02-14 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0005_auto_20220214_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutusseodetailsmodel',
            name='title',
            field=models.CharField(max_length=106),
        ),
    ]
