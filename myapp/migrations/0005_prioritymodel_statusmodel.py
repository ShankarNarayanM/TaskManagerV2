# Generated by Django 5.1.4 on 2025-01-28 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriorityModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StatusModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100)),
            ],
        ),
    ]
