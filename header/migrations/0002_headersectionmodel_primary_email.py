# Generated by Django 2.2.27 on 2022-03-04 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('header', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='headersectionmodel',
            name='primary_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]