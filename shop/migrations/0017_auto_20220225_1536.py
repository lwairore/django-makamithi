# Generated by Django 2.2.27 on 2022-02-25 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_two', '0024_auto_20220214_1209'),
        ('shop', '0016_auto_20220223_1518'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=70)),
                ('review', models.TextField(max_length=5000)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('client_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='home_two.PhotoModel')),
            ],
            options={
                'verbose_name': 'Product review',
                'verbose_name_plural': 'Product reviews',
            },
        ),
        migrations.AddField(
            model_name='productmodel',
            name='reviews',
            field=models.ManyToManyField(blank=True, to='shop.ProductReview'),
        ),
    ]
