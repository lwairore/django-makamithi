# Generated by Django 2.2.27 on 2022-03-09 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0022_auto_20220309_0744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientreviewsectionmodel',
            name='background_image',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='client_review_section_background_image', to='home_two.PhotoModel'),
        ),
        migrations.AlterField(
            model_name='clientreviewsectionmodel',
            name='section_image',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='client_review_section_section_image', to='home_two.PhotoModel'),
        ),
    ]
