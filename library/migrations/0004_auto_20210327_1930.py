# Generated by Django 3.1.7 on 2021-03-27 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20210322_1642'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='program',
            new_name='program_name',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='semester',
            new_name='semester_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='type',
        ),
        migrations.AddField(
            model_name='note',
            name='added_by',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='note',
            name='date_of_added',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='note',
            name='date_of_modified',
            field=models.DateField(auto_now=True),
        ),
    ]