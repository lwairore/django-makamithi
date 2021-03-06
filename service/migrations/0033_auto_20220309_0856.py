# Generated by Django 2.2.27 on 2022-03-09 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0032_auto_20220309_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicemodel',
            name='about_photo',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='service_model_about_photo', to='home_two.PhotoModel'),
        ),
        migrations.AlterField(
            model_name='servicemodel',
            name='home_photo',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='service_model_home_photo', to='home_two.PhotoModel'),
        ),
        migrations.AlterField(
            model_name='servicemodel',
            name='service_detail_photo',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='service_model_service_detail_photo', to='home_two.PhotoModel'),
        ),
        migrations.AlterField(
            model_name='servicemodel',
            name='service_page_photo',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='service_model_service_page_photo', to='home_two.PhotoModel'),
        ),
    ]
