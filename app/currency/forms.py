from django import forms
from .models import Source
from .models import ContactUs
from .models import Rate
from django.contrib.auth.forms import PasswordChangeForm

class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ['buy', 'sell', 'currency', 'source']

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'reply_to', 'subject', 'body']


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = ['name', 'source_url', 'exchange_address', 'phone_number']


class SupportForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=128)
    reply_to = forms.EmailField(label='Email для ответа')
    subject = forms.CharField(label='Тема', max_length=128)
    body = forms.CharField(label='Сообщение', widget=forms.Textarea)



class CustomPasswordChangeForm(PasswordChangeForm):
    current_password = forms.CharField(
        label="Current Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )


