# Generated by Django 5.1.4 on 2025-01-28 15:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_alter_taskboard_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskboard',
            name='status',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.statusmodel'),
        ),
    ]
