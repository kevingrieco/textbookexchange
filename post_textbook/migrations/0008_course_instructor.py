# Generated by Django 4.1.2 on 2022-12-07 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_textbook', '0007_alter_textbook_isbn'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.CharField(default='INSTRUCTOR', max_length=200),
            preserve_default=False,
        ),
    ]
