# Generated by Django 2.2.27 on 2022-02-27 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0004_contactusseodetailsmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactusseodetailsmodel',
            name='keywords',
            field=models.CharField(blank=True, max_length=160, null=True),
        ),
    ]