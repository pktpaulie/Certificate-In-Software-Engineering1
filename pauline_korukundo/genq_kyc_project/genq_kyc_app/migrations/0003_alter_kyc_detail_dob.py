# Generated by Django 4.1.7 on 2023-04-28 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genq_kyc_app', '0002_rename_kyc_details_kyc_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kyc_detail',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]
