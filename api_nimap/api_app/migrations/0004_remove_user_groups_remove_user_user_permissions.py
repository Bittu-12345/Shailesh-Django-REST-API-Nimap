# Generated by Django 5.0 on 2024-05-12 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0003_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
    ]
