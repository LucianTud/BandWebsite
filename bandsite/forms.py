# bandsite/forms.py

from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'rating', 'comment']


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Nume')
    email = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea, label='Mesaj')
