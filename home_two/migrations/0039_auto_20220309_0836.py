# Generated by Django 2.2.27 on 2022-03-09 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_two', '0038_auto_20220309_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whychooseussectionmodel',
            name='section_image',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='why_choose_us_section_section_image', to='home_two.PhotoModel'),
        ),
    ]
