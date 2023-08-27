from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Rate, ContactUs, Source
from .forms import SourceForm

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