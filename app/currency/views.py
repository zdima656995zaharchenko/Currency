from django.shortcuts import render, redirect
from .models import Rate, ContactUs, Source
from .forms import SourceForm

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

