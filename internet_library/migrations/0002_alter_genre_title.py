# Generated by Django 4.0.8 on 2023-07-30 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internet_library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
