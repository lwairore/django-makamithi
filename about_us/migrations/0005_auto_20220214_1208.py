# Generated by Django 2.2.27 on 2022-02-14 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0004_aboutusseodetailsmodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutusseodetailsmodel',
            options={'verbose_name': 'About Us SEO Detail', 'verbose_name_plural': 'About Us SEO Details'},
        ),
        migrations.AlterField(
            model_name='aboutusseodetailsmodel',
            name='title',
            field=models.CharField(max_length=80),
        ),
    ]
