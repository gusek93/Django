# Generated by Django 3.0.14 on 2021-09-29 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0003_auto_20210928_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_public',
            field=models.BooleanField(default=False, verbose_name='공개여부'),
        ),
    ]