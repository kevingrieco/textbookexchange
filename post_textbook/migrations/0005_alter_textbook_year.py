# Generated by Django 4.1.2 on 2022-10-18 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_textbook', '0004_textbook_course_textbook_cover_textbook_department_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textbook',
            name='year',
            field=models.IntegerField(),
        ),
    ]
