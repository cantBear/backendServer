# Generated by Django 3.2.16 on 2023-03-14 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfolders', '0002_auto_20230312_1049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='folder',
            name='email_domain',
        ),
    ]
