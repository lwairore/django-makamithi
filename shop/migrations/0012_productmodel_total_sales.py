# Generated by Django 2.2.27 on 2022-02-23 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_shopseodetailsmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='total_sales',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
