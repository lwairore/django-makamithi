# Generated by Django 2.2.27 on 2022-03-09 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0025_auto_20220309_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamareasectionmodel',
            name='section_image',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='home_two.PhotoModel'),
        ),
    ]
