# Generated by Django 3.1.2 on 2020-10-08 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20200901_1306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forumpost',
            name='image',
        ),
    ]