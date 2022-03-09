# Generated by Django 2.2.27 on 2022-02-10 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_two', '0003_auto_20220210_1648'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutSectionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=70)),
                ('description', models.TextField(blank=True, max_length=250, null=True)),
                ('photo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='home_two.PhotoModel')),
            ],
            options={
                'verbose_name': 'About section',
                'verbose_name_plural': 'About sections',
            },
        ),
    ]