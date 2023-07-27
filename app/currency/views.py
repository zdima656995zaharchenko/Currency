# currency/views.py
from django.shortcuts import render
from .models import ContactUs

def contact_us_list(request):
    contacts = ContactUs.objects.all()
    return render(request, 'currency/contact_us_list.html', {'contacts': contacts})

