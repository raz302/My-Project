# Generated by Django 3.1.2 on 2020-10-12 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20201008_0512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artisan',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='artisan',
            name='github',
        ),
    ]
