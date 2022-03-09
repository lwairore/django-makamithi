# Generated by Django 2.2.27 on 2022-03-01 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_two', '0026_auto_20220228_1344'),
    ]

    operations = [
        migrations.CreateModel(
            name='BadgeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_years', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Badge',
                'verbose_name_plural': 'Badges',
            },
        ),
        migrations.CreateModel(
            name='CounterAreaSectionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=60)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('background_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='home_two.PhotoModel')),
            ],
            options={
                'verbose_name': 'Counter area section',
                'verbose_name_plural': 'Counter area section',
            },
        ),
    ]