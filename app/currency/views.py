from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Rate, ContactUs, Source
from .forms import SourceForm, ContactUsForm
from django.views.generic import TemplateView
from django.http import HttpResponseServerError
from django.views.generic.edit import FormView
from .forms import SupportForm
from .forms import RateForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import user_passes_test


class RateListView(ListView):
    model = Rate
    template_name = 'rate_list.html'
    context_object_name = 'rates'

class RateCreateView(CreateView):
    model = Rate
    form_class = RateForm
    template_name = 'rate_create.html'
    success_url = reverse_lazy('rate_list')

def is_superuser(user):
    return user.is_superuser

class RateUpdateView(UpdateView):
    model = Rate
    form_class = RateForm
    template_name = 'rate_update.html'
    success_url = reverse_lazy('rate_list')

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Rate, pk=pk)

class RateDeleteView(DeleteView):
    model = Rate
    template_name = 'rate_delete.html'
    success_url = reverse_lazy('rate_list')

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Rate, pk=pk)

class RateDetailView(LoginRequiredMixin, DetailView):
    model = Rate
    template_name = 'rate_details.html'
    succes_url = reverse_lazy('rate_list')



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

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Обновляем хэш сессии
            return redirect('password_change_done')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})
