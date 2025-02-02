# Generated by Django 4.1.7 on 2023-04-28 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kyc_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=50, null=True)),
                ('lastname', models.CharField(blank=True, max_length=50, null=True)),
                ('dob', models.DateField(blank=True)),
                ('gender', models.CharField(blank=True, choices=[('FEMALE', 'Female'), ('MALE', 'Male')], max_length=10)),
                ('country', models.CharField(blank=True, max_length=50)),
                ('district', models.CharField(blank=True, max_length=100)),
                ('town', models.CharField(blank=True, max_length=100)),
                ('zip_code', models.CharField(blank=True, max_length=15)),
                ('phone_num1', models.IntegerField(blank=True, default=0)),
                ('phone_num2', models.IntegerField(blank=True, default=0, null=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
