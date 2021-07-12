# Generated by Django 3.0 on 2021-06-18 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_auto_20210327_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='file',
            field=models.FileField(blank=True, upload_to='notice'),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
                ('course_code', models.CharField(max_length=10)),
                ('credit_hrs', models.IntegerField()),
                ('program_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='library.Program')),
                ('semester', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='library.Semester')),
            ],
        ),
    ]