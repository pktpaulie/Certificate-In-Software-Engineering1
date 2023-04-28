from django.urls import path
from genq_kyc_app import views
from .views import kyc

urlpatterns = [
    path('kyc/', views.kyc, name='kyc')
]
