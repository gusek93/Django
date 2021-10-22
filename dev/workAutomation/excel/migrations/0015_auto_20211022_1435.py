# Generated by Django 3.0.14 on 2021-10-22 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excel', '0014_auto_20211018_0805'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentDivision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('uploadedFile', models.FileField(upload_to='paymentDivision/')),
                ('dateTimeOfUpload', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaxfreeSubtraction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('uploadedFile', models.FileField(upload_to='taxfreeSubtraction/')),
                ('dateTimeOfUpload', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='SalaryCalculate',
        ),
        migrations.DeleteModel(
            name='SalarySum',
        ),
    ]
