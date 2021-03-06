# Generated by Django 2.2.27 on 2022-03-09 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_two', '0031_auto_20220309_0741'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutsectionmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='aboutsectionmodel',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='aboutsectionmodel',
            name='photo',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='home_two.PhotoModel'),
        ),
    ]
