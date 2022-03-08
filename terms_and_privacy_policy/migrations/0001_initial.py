# Generated by Django 2.2.27 on 2022-02-28 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PrivacyPolicyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(max_length=180)),
                ('content', models.TextField(max_length=5000)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Privacy policy',
                'verbose_name_plural': 'Privacy policy',
            },
        ),
    ]
