# Generated by Django 5.1.4 on 2025-01-14 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_user_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
    ]
