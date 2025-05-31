# bandsite/forms.py

from django import forms
from .models import Review
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import MediaItem

class MediaItemForm(forms.ModelForm):
    class Meta:
        model = MediaItem
        fields = ['title', 'media_type', 'image', 'video_url', 'category']
        widgets = {
            'media_type': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titlul media'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'video_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://youtube.com/...'}),
            'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Eveniment 2024'}),
        }


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Adaugă placeholder gol pentru animația etichetei în stil login.html
        for field in self.fields.values():
            field.widget.attrs.update({
                'placeholder': ' ',
                'class': 'form-control',  # pentru a păstra stilul Bootstrap/form-floating
            })

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'rating', 'comment']


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Nume')
    email = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea, label='Mesaj')
