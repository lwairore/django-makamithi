# Generated by Django 2.2.27 on 2022-03-01 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_two', '0027_badgemodel_counterareasectionmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counterareasectionmodel',
            name='heading',
            field=models.CharField(max_length=80),
        ),
    ]