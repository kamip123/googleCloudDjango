# Generated by Django 2.1.2 on 2018-11-18 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cityMap', '0003_auto_20181104_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='cityowned',
            name='is_capital',
            field=models.BooleanField(default=False),
        ),
    ]
