# Generated by Django 3.0.6 on 2020-06-11 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0004_auto_20200610_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='publist',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
