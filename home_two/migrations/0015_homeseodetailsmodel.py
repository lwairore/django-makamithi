# Generated by Django 2.2.27 on 2022-02-12 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social_sharing', '0009_delete_seosocialsharedatamodel'),
        ('home_two', '0014_whychooseussectionmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeSEODetailsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('keywords', models.CharField(blank=True, max_length=80, null=True)),
                ('description', models.TextField(blank=True, max_length=180, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=80, null=True)),
                ('author', models.CharField(blank=True, max_length=160, null=True)),
                ('section', models.CharField(blank=True, max_length=160, null=True)),
                ('published', models.DateTimeField(auto_now=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='social_sharing.ImageAuxDataModel')),
            ],
            options={
                'verbose_name': 'Home SEO Detail',
                'verbose_name_plural': 'Home SEO Details',
            },
        ),
    ]