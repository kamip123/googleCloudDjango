# Generated by Django 2.1.2 on 2018-12-04 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0005_auto_20181204_2111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='published_date',
        ),
    ]
