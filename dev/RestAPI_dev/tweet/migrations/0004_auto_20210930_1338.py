# Generated by Django 3.0.14 on 2021-09-30 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0003_auto_20210930_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweets',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]