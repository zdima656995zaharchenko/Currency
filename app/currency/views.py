from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Rate, ContactUs, Source
from .forms import SourceForm, ContactUsForm
from django.views.generic import TemplateView
from django.http import HttpResponseServerError
from django.views.generic.edit import FormView
from .forms import SupportForm









class SourceListView(ListView):
    model = Source
    template_name = 'source_list.html'
    context_object_name = 'sources'

class SourceCreateView(CreateView):
    model = Source
    form_class = SourceForm
    template_name = 'source_create.html'
    success_url = reverse_lazy('source_list')

class SourceUpdateView(UpdateView):
    model = Source
    form_class = SourceForm
    template_name = 'source_update.html'
    success_url = reverse_lazy('source_list')

class SourceDeleteView(DeleteView):
    model = Source
    form_class = SourceForm
    template_name = 'source_delete.html'
    success_url = reverse_lazy('source_list')

def rates_view(request):
    rates = Rate.objects.all()
    return render(request, 'rates.html', {'rates': rates})

def contact_view(request):
    return render(request, 'contact.html')

def contact_us_list(request):
    contacts = ContactUs.objects.all()
    return render(request, 'currency/contact_us_list.html', {'contacts': contacts})

def source_details(request, pk):
    source = Source.objects.get(pk=pk)
    return render(request, 'source_details.html', {'source': source})


def source_delete():
    return None

class IndexView(TemplateView):
    template_name = 'index.html'





class ContactUsCreateView(CreateView):
    model = ContactUs
    template_name = 'contactus_create.html'
    success_url = reverse_lazy('index')
    form_class = ContactUsForm

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        recipient = settings.EMAIL_HOST_USER
        subject = 'User Contact Us'
        body = f'''
           Request from: {cleaned_data['name']}.
           Email to reply: {cleaned_data['reply_to']}
           Subject: {cleaned_data['subject']}
           Body: {cleaned_data['body']}
           '''
        send_mail(
            subject,
            body,
            recipient,
            [recipient],
            fail_silently=False
        )

        return super().form_valid(form)

