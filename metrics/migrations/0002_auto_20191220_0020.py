# Generated by Django 3.0 on 2019-12-20 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientmetrics',
            name='attributes',
            field=models.CharField(default='{}', max_length=1024),
        ),
        migrations.AlterField(
            model_name='patientmetrics',
            name='notes',
            field=models.CharField(max_length=1024),
        ),
    ]