# Generated by Django 5.1.2 on 2024-11-12 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]
