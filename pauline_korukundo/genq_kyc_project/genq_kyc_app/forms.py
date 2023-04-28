from django import forms
from django.contrib.auth.models import User
from .models import Kyc_Detail


# class KycForm(forms.ModelForm):
#     MALE = 'M'
#     FEMALE = 'F'
#     GENDER_CHOICES = (
#     (MALE, 'male'),
#     (FEMALE, 'female'),
#     )

    
#     COUNTRY_CHOICES = (
#     ('Ug', 'Uganda'),
#     ('Ke', 'Kenya'),
#     ('Tz', 'Tanzania'),
#     ('Rw', 'Rwanda'),
#     ('Burundi', 'Burundi'),    
#     )

#     firstname = forms.CharField(required = True, help_text = "Enter your First Name")
#     lastname = forms.CharField(required = True, help_text = "Enter your Last Name")
#     date_of_birth = forms.DateField(null=True)
#     gender = forms.ChoiceField(choices = GENDER_CHOICES, required = True, 
#         help_text = "Select your Gender")
#     country = forms.ChoiceField(choices=COUNTRY_CHOICES, required = True, help_text = "Enter your Country")
#     district = forms.CharField()  
#     town = forms.CharField()
#     zip_code = forms.CharField()
#     phone_num1 = forms.IntegerField()
#     phone_num2 = forms.IntegerField()
#     email = forms.EmailField()

#     class Meta:
#         model = Kyc_Detail
#         fields = ('__all__')