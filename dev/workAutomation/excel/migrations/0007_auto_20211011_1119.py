# Generated by Django 3.0.14 on 2021-10-11 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excel', '0006_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='uploadedFile',
            field=models.FileField(upload_to='급상여/'),
        ),
    ]