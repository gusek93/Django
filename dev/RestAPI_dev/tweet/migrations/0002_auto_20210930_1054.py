# Generated by Django 3.0.14 on 2021-09-30 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweets',
            name='url',
            field=models.TextField(null=True),
        ),
    ]
