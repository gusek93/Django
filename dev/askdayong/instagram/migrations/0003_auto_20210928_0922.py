# Generated by Django 3.0.14 on 2021-09-28 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0002_auto_20210928_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='message',
            field=models.TextField(),
        ),
    ]