# Generated by Django 3.0.14 on 2021-10-10 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileupload',
            name='content',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
