# Generated by Django 3.1.7 on 2021-03-27 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_auto_20210327_1943'),
    ]

    operations = [
        migrations.RenameField(
            model_name='program',
            old_name='semester_name',
            new_name='semester',
        ),
        migrations.RenameField(
            model_name='semester',
            old_name='semester_name',
            new_name='semester',
        ),
    ]