# Generated by Django 2.2.27 on 2022-02-12 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_two', '0012_visitnowctasectionmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitnowctasectionmodel',
            name='description',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]
