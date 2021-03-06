# Generated by Django 2.1.2 on 2018-12-16 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('premium', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('currency', models.CharField(default='EUR', max_length=3)),
                ('status', models.CharField(blank=True, choices=[('W', 'Waiting for payment'), ('P', 'Payment complete')], default='W', max_length=1)),
            ],
        ),
    ]
