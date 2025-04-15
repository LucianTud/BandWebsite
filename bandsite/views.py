from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from .models import Member, Album, Concert
from .forms import ContactForm
from django.core.mail import send_mail
from django.http import HttpResponse
# rom .models import Review


def home(request):
    return render(request, 'bandsite/home.html')

def about(request):
    return render(request, 'bandsite/about.html')

def gallery(request):
    return render(request, 'bandsite/gallery.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cont creat cu succes!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'bandsite/register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'bandsite/login.html'



def members(request):
    members = Member.objects.all()
    return render(request, 'bandsite/members.html', {'members': members})

def albums(request):
    albums = Album.objects.all()
    return render(request, 'bandsite/albums.html', {'albums': albums})

def concerts(request):
    concerts = Concert.objects.all().order_by('date')
    return render(request, 'bandsite/concerts.html', {'concerts': concerts})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Colectăm datele
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Trimitem email
            send_mail(
                f'Mesaj de la {name}',
                message,
                email,  # From
                ['trupe@site.com'],  # To
            )
            return render(request, 'bandsite/contact_success.html')
    else:
        form = ContactForm()

    return render(request, 'bandsite/contact.html', {'form': form})

  # Presupunând că ai un model Review

def submit_review(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        # Salvăm recenzia în baza de date
        Review.objects.create(name=name, rating=rating, comment=comment)

        # Redirecționăm utilizatorul înapoi la pagina de Home sau la o altă pagină
        return redirect('home')

    return HttpResponse("Invalid request method", status=400)

