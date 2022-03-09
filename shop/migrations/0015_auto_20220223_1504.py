# Generated by Django 2.2.27 on 2022-02-23 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_two', '0024_auto_20220214_1209'),
        ('shop', '0014_productmodel_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='photo',
        ),
        migrations.AddField(
            model_name='productmodel',
            name='product_preview',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='photo_model_product_preview', to='home_two.PhotoModel'),
        ),
    ]