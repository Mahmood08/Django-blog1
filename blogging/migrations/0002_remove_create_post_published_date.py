# Generated by Django 2.1.1 on 2019-08-10 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='create_post',
            name='published_date',
        ),
    ]
