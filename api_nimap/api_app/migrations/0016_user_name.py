# Generated by Django 5.0 on 2024-05-12 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0015_rename_name_project_project_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
