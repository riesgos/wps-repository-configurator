# Generated by Django 4.2.2 on 2023-06-16 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_processinput_schema_alter_processinput_input_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='processinput',
            name='command_line_flag',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='processoutput',
            name='read_from',
            field=models.CharField(choices=[('file', 'file'), ('stdout', 'stdout')], max_length=64),
        ),
    ]
