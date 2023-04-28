from django.shortcuts import render, redirect
from .models import Kyc_Detail
from django.contrib import messages
# from .forms import KycForm

def kyc(request):
    if request.method == 'POST':
        
        firstname_field = request.POST.get('firstname')
        lastname_field = request.POST.get('lastname')
        date_of_birth_field = request.POST.get('date_of_birth')
        gender_field = request.POST.get('gender')
        country_field = request.POST.get('country')
        district_field = request.POST.get('district')
        town_field = request.POST.get('town')
        zip_code_field = request.POST.get('zip_code')
        phone_num1_field = request.POST.get('phone_num1')
        phone_num2_field = request.POST.get('phone_num2')
        email_field = request.POST.get('email')

        kyc_details = Kyc_Detail(
            firstname=firstname_field, 
            lastname=lastname_field,
            date_of_birth=date_of_birth_field,
            gender=gender_field,
            country=country_field,
            district=district_field,
            town=town_field,
            zip_code=zip_code_field,
            phone_num1=phone_num1_field,
            phone_num2=phone_num2_field,
            email=email_field
            )
        if kyc_details.clean:
            kyc_details.save()
        #kyc_details.save()
        #return render(request, 'kyc')
            messages.success(request, 'Successful')
        # reloading the form once kyc details are successfully saved
            return redirect('/kyc')
            #return render(request, '/kyc')
    else:
        print('Not posted')

    captured_details = Kyc_Detail.objects.all()
    return render(request, 'kyc.html', {'captured_details':captured_details})

# def kyc(request):
#     form = KycForm()
#     if request.method == 'POST':
#         if form.is_valid():
#             data = form.save(commit=False)
#             data.firstname = request.firstname_field
#             data.lastname = request.lastname_field
#             data.date_of_birth = request.date_of_birth_field
#             data.gender = request.gender_field
#             data.country = request.country_field
#             data.district = request.district_field
#             data.town = request.town_field
#             data.zip_code = request.zip_code_field
#             data.phone_num1 = request.phone_num1_field
#             data.phone_num2 = request.phone_num2_field
#             data.email = request.email_field
#             return redirect('/kyc')
#         else:
#             form = KycForm
#         return render(request, 'kyc.html', {'form':form})