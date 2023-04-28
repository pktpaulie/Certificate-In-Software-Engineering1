from django.db import models


class Kyc_Detail(models.Model):
    GENDER_CHOICES = [
        ('FEMALE', 'Female'),
        ('MALE', 'Male'),
        ]
    firstname = models.CharField(max_length=50, null=True, blank=True)
    lastname = models.CharField(max_length=50, null=True, blank=True)
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=10, null=True, blank=True, choices=GENDER_CHOICES)
    country = models.CharField(max_length=50, null=True, blank=True)
    district = models.CharField(max_length=100, null=True, blank=True)
    town = models.CharField(max_length=100,null=True, blank=True)
    zip_code = models.CharField(max_length=15, null=True, blank=True)
    phone_num1 = models.IntegerField(default=0, null=True, blank=True)
    phone_num2 = models.IntegerField(default=0, null=True, blank=True)
    email = models.EmailField(null=True)


    # def __str__(self):
    #     return self.firstname