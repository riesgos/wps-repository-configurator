# Generated by Django 4.2.2 on 2023-06-16 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_processinput_processinputallowedvalue'),
    ]

    operations = [
        migrations.AddField(
            model_name='processinput',
            name='allowed_values',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.DeleteModel(
            name='ProcessInputAllowedValue',
        ),
    ]
