# Generated by Django 2.2.27 on 2022-02-22 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0020_auto_20220221_2130'),
    ]

    operations = [
        migrations.CreateModel(
            name='BenefitModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Benefit',
                'verbose_name_plural': 'Benefits',
            },
        ),
        migrations.RemoveField(
            model_name='planmodel',
            name='description',
        ),
        migrations.RemoveField(
            model_name='planmodel',
            name='title',
        ),
        migrations.AddField(
            model_name='planmodel',
            name='benefits',
            field=models.ManyToManyField(blank=True, to='service.BenefitModel'),
        ),
    ]
