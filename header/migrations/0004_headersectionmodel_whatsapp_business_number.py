# Generated by Django 2.2.27 on 2022-03-04 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('header', '0003_auto_20220304_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='headersectionmodel',
            name='whatsapp_business_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]