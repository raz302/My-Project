# Generated by Django 3.1.2 on 2020-10-18 08:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20201012_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
