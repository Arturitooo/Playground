# Generated by Django 4.2.1 on 2023-09-15 20:12

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Todos',
            new_name='Task',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='todopoint',
            new_name='task',
        ),
    ]
