# Generated by Django 2.2.27 on 2022-02-11 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_two', '0010_auto_20220211_1626'),
        ('shop', '0006_productmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='home_two.PhotoModel'),
        ),
    ]
