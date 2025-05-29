from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from .models import Member, Album, Concert
from .forms import ContactForm
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import Review
from .forms import ReviewForm
from django.http import JsonResponse
from django.core.paginator import Paginator


def submit_review(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        # Verificăm dacă câmpurile nu sunt goale
        if name and rating and comment:
            # Salvăm recenzia în baza de date
            Review.objects.create(name=name, rating=rating, comment=comment)

            # Mesaj de succes
            messages.success(request, 'Recenzia ta a fost adăugată cu succes!')
            return redirect('home')  # Redirecționăm utilizatorul către pagina de Home
        else:
            messages.error(request, 'Te rugăm să completezi toate câmpurile!')
            return redirect('home')
    return HttpResponse("Invalid request method", status=400)

def load_more_reviews(request):
    reviews = Review.objects.all().order_by('-created_at')
    paginator = Paginator(reviews, 4)  # 4 recenzii pe pagină
    page = request.GET.get('page', 1)  # Dacă nu se specifică pagina, începe de la 1
    reviews_page = paginator.get_page(page)

    reviews_data = []
    for review in reviews_page:
        reviews_data.append({
            'name': review.name,
            'comment': review.comment,
            'rating': review.rating,
            'created_at': review.created_at.strftime('%d-%m-%Y'),
        })

    return JsonResponse({'reviews': reviews_data})





def home(request):
    # Obține primele 4 recenzii ordonate după data de creare (descrescător)
    reviews = Review.objects.all().order_by('-created_at')[:4]  # Primele 4 recenzii
    all_reviews_count = Review.objects.count()  # Contorul total al recenziilor
    return render(request, 'bandsite/home.html', {'reviews': reviews, 'all_reviews_count': all_reviews_count})






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




