# Generated by Django 2.2.27 on 2022-02-10 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_two', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerAdModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('description', models.TextField(blank=True, max_length=250, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('photos', models.ManyToManyField(blank=True, to='home_two.PhotoModel')),
            ],
            options={
                'verbose_name': 'Banner ad',
                'verbose_name_plural': 'Banner ads',
            },
        ),
    ]