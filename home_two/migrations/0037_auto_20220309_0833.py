# Generated by Django 2.2.27 on 2022-03-09 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_two', '0036_auto_20220309_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productareasectionmodel',
            name='section_image',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='home_two.PhotoModel'),
        ),
    ]
