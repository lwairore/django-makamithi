# Generated by Django 2.2.27 on 2022-02-11 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_two', '0006_auto_20220210_2037'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureSectionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=10)),
                ('description', models.TextField(blank=True, max_length=250, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('photo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='home_two.PhotoModel')),
            ],
            options={
                'verbose_name': 'Feature section',
                'verbose_name_plural': 'Feature sections',
            },
        ),
    ]
