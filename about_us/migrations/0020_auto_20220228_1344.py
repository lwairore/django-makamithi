# Generated by Django 2.2.27 on 2022-02-28 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0019_auto_20220227_1206'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apaboutsectionmodel',
            options={'verbose_name': 'Ap About section', 'verbose_name_plural': 'Ap About section'},
        ),
        migrations.AlterModelOptions(
            name='clientreviewsectionmodel',
            options={'verbose_name': 'Client review section', 'verbose_name_plural': 'Client review section'},
        ),
        migrations.AlterModelOptions(
            name='faqsectionmodel',
            options={'verbose_name': 'Faq section', 'verbose_name_plural': 'Faq section'},
        ),
        migrations.AlterModelOptions(
            name='teamareasectionmodel',
            options={'verbose_name': 'Team area section', 'verbose_name_plural': 'Team area section'},
        ),
        migrations.AlterModelOptions(
            name='whatwedosectionmodel',
            options={'verbose_name': 'What we do section', 'verbose_name_plural': 'What we do section'},
        ),
    ]
