# Generated by Django 4.2.2 on 2023-06-16 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_process_working_dir'),
    ]

    operations = [
        migrations.AddField(
            model_name='processinput',
            name='schema',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='processinput',
            name='input_type',
            field=models.CharField(choices=[('bbox', 'bounding box'), ('double', 'double'), ('string', 'string'), ('quakeml', 'quakeml')], max_length=64),
        ),
    ]
