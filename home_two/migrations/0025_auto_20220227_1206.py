# Generated by Django 2.2.27 on 2022-02-27 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_two', '0024_auto_20220214_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeseodetailsmodel',
            name='keywords',
            field=models.CharField(blank=True, max_length=160, null=True),
        ),
    ]
