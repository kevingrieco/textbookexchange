# Generated by Django 4.1.2 on 2022-11-06 17:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('direct_messages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='latest',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
