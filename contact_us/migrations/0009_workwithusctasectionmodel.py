# Generated by Django 2.2.27 on 2022-03-03 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_two', '0030_productareasectionmodel'),
        ('contact_us', '0008_auto_20220228_1344'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkWithUsCtaSectionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=60)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('call_to_action', models.CharField(max_length=70)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('background_image', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='work_with_us_cta_section_background_image', to='home_two.PhotoModel')),
                ('section_image', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='work_with_us_cta_section_section_image', to='home_two.PhotoModel')),
            ],
            options={
                'verbose_name': 'Work with us cta section',
                'verbose_name_plural': 'Work with us cta section',
            },
        ),
    ]