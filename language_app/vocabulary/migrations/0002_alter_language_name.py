# Generated by Django 5.2.1 on 2025-06-08 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocabulary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
