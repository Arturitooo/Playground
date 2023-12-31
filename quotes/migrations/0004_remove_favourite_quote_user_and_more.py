# Generated by Django 4.2.1 on 2023-11-05 15:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quotes', '0003_alter_favourite_quote_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favourite_quote',
            name='user',
        ),
        migrations.AlterField(
            model_name='favourite_quote',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='favourite_quote',
            name='quote',
            field=models.CharField(max_length=150),
        ),
    ]
