# Generated by Django 3.1.2 on 2020-10-08 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myAuth', '0002_myuser_is_artisan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='photo',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]
