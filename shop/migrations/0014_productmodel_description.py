# Generated by Django 2.2.27 on 2022-02-23 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_productmodel_keywords'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='description',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
    ]