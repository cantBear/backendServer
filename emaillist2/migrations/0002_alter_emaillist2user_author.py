# Generated by Django 3.2.16 on 2023-02-16 04:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('emaillist2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emaillist2user',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user'),
        ),
    ]
