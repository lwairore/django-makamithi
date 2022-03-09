# Generated by Django 2.2.27 on 2022-02-16 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_two', '0024_auto_20220214_1209'),
        ('service', '0004_auto_20220216_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicemodel',
            name='about_photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='service_model_about_photo', to='home_two.PhotoModel'),
        ),
        migrations.AlterField(
            model_name='servicemodel',
            name='home_photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='service_model_home_photo', to='home_two.PhotoModel'),
        ),
    ]