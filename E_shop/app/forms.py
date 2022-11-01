from django import forms
from .models import Mail


class MailForm(forms.Form):
    class Meta:
        model = Mail
        fields = ('email',)
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'})
        }
