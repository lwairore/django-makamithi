# Generated by Django 2.2.27 on 2022-02-21 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0019_auto_20220221_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicemodel',
            name='description',
            field=models.TextField(blank=True, max_length=1200, null=True),
        ),
    ]
