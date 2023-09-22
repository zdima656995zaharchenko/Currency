from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import Rate, ContactUs, Source
from .forms import SourceForm, ContactUsForm
from django.views.generic import TemplateView
from django.http import HttpResponseServerError
from django.views.generic.edit import FormView
from .forms import SupportForm

def rates_view(request):
    rates = Rate.objects.all()
    return render(request, 'rates.html', {'rates': rates})

def contact_view(request):
    return render(request, 'contact.html')

def contact_us_list(request):
    contacts = ContactUs.objects.all()
    return render(request, 'currency/contact_us_list.html', {'contacts': contacts})

def source_list(request):
    sources = Source.objects.all()
    return render(request, 'source_list.html', {'sources': sources})

def source_create(request):
    if request.method == 'POST':
        form = SourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('source_list')
    else:
        form = SourceForm()
    return render(request, 'source_create.html', {'form': form})

def source_update(request, pk):
    source = Source.objects.get(pk=pk)
    if request.method == 'POST':
        form = SourceForm(request.POST, instance=source)
        if form.is_valid():
            form.save()
            return redirect('source_list')
    else:
        form = SourceForm(instance=source)
    return render(request, 'source_update.html', {'form': form})

def source_details(request, pk):
    source = Source.objects.get(pk=pk)
    return render(request, 'source_details.html', {'source': source})

def source_delete(request, pk):
    source = Source.objects.get(pk=pk)
    source.delete()
    return redirect('source_list')

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

