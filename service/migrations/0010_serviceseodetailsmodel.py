# Generated by Django 2.2.27 on 2022-02-20 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_two', '0024_auto_20220214_1209'),
        ('service', '0009_servicemodel_plans'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceSEODetailsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=106)),
                ('keywords', models.CharField(blank=True, max_length=80, null=True)),
                ('description', models.TextField(blank=True, max_length=466, null=True)),
                ('type', models.CharField(blank=True, max_length=80, null=True)),
                ('author', models.CharField(blank=True, max_length=160, null=True)),
                ('section', models.CharField(blank=True, max_length=160, null=True)),
                ('published', models.DateTimeField(auto_now=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='home_two.PhotoModel')),
            ],
            options={
                'verbose_name': 'About Us SEO Detail',
                'verbose_name_plural': 'About Us SEO Details',
            },
        ),
    ]
