# Generated by Django 3.0 on 2021-07-12 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20210713_0003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='credit_hrs',
        ),
    ]
