# Generated by Django 4.2.1 on 2023-11-02 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seotool', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keywords_suggestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_keyword', models.CharField(max_length=150)),
                ('keywords_suggested', models.CharField(max_length=10000)),
                ('publication_date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='GoogleSearchResult',
        ),
    ]