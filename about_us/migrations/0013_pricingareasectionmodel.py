# Generated by Django 2.2.27 on 2022-02-17 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_two', '0024_auto_20220214_1209'),
        ('about_us', '0012_clientreviewsectionmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='PricingAreaSectionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=80)),
                ('summary', models.TextField(blank=True, max_length=250, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('section_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='home_two.PhotoModel')),
            ],
            options={
                'verbose_name': 'Pricing area section',
                'verbose_name_plural': 'Pricing area sections',
            },
        ),
    ]