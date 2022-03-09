# Generated by Django 2.2.27 on 2022-03-09 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_two', '0030_productareasectionmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeseodetailsmodel',
            name='image',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='home_two.PhotoModel'),
        ),
        migrations.AlterField(
            model_name='homeseodetailsmodel',
            name='published',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
