# Generated by Django 2.1.2 on 2018-12-01 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alliance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alliance',
            name='alliance_logo',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
