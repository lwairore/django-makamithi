# Generated by Django 2.2.27 on 2022-02-14 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_two', '0024_auto_20220214_1209'),
        ('about_us', '0006_auto_20220214_1209'),
    ]

    operations = [
        migrations.CreateModel(
            name='FaqSectionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('background_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='home_two.PhotoModel')),
            ],
            options={
                'verbose_name': 'Faq section',
                'verbose_name_plural': 'Faq sections',
            },
        ),
    ]
