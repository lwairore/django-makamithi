# Generated by Django 2.2.27 on 2022-02-25 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_auto_20220225_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='productreview',
            name='rating',
            field=models.CharField(choices=[('5', 'Five stars'), ('4', 'Four stars'), ('3', 'Three stars'), ('2', 'Two stars'), ('1', 'One star')], default='5', max_length=11),
        ),
    ]