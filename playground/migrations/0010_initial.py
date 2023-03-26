# Generated by Django 4.1.7 on 2023-03-24 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('playground', '0009_delete_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('startTime', models.TimeField(default=None)),
                ('date', models.DateField(default=None)),
                ('footfall', models.IntegerField(default=0)),
                ('venue', models.CharField(max_length=255)),
                ('state', models.CharField(choices=[('AP', 'Andhra Pradesh'), ('AR', 'Arunachal Pradesh'), ('AS', 'Assam'), ('BR', 'Bihar'), ('CG', 'Chhattisgarh'), ('GA', 'Goa'), ('GJ', 'Gujarat'), ('HR', 'Haryana'), ('HP', 'Himachal Pradesh'), ('JK', 'Jammu and Kashmir'), ('JH', 'Jharkhand'), ('KA', 'Karnataka'), ('KL', 'Kerala'), ('MP', 'Madhya Pradesh'), ('MH', 'Maharashtra'), ('MN', 'Manipur'), ('ML', 'Meghalaya'), ('MZ', 'Mizoram'), ('NL', 'Nagaland'), ('OD', 'Odisha'), ('PB', 'Punjab'), ('RJ', 'Rajasthan'), ('SK', 'Sikkim'), ('TN', 'Tamil Nadu'), ('TS', 'Telangana'), ('TR', 'Tripura'), ('UK', 'Uttarakhand'), ('UP', 'Uttar Pradesh'), ('WB', 'West Bengal'), ('DL', 'Delhi')], default='DL', max_length=2)),
                ('image', models.URLField(default=None)),
                ('slug', models.SlugField(default=None, max_length=255)),
            ],
        ),
    ]
