# Generated by Django 4.1.7 on 2023-03-22 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0003_remove_event_footfall'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='footfall',
            field=models.IntegerField(default=0),
        ),
    ]
