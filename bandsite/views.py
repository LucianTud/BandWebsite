from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from .models import Member, Album, Concert, Review
from .forms import ContactForm, ReviewForm, CustomUserCreationForm
from .models import MediaItem
from .forms import MediaItemForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .utils import extract_youtube_video_id  # Importă funcția utilitară
from django.shortcuts import render, redirect, get_object_or_404
from .models import MediaItem
from django.http import Http404
from django.contrib.auth import logout


def delete_media(request, media_id):
    try:
        media_item = MediaItem.objects.get(id=media_id)
        media_item.delete()
    except MediaItem.DoesNotExist:
        raise Http404("Media item not found")

    # Redirecționează către pagina galeriei după ștergere
    return redirect('gallery')


# Doar superuserii sau staff-ul pot adăuga
def is_admin(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(is_admin)
def add_media(request):
    if request.method == 'POST':
        form = MediaItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Media adăugată cu succes!")
            return redirect('gallery')
    else:
        form = MediaItemForm()

    return render(request, 'bandsite/add_media.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('home')

def gallery(request):
    media_items = MediaItem.objects.all()  # Poți adăuga filtre dacă e necesar

    # Extragem ID-ul video-ului YouTube pentru fiecare media de tip 'video'
    for item in media_items:
        if item.media_type == 'video' and item.video_url:
            item.video_embed_url = extract_youtube_video_id(item.video_url)

    return render(request, 'bandsite/gallery.html', {'media_items': media_items})



def home(request):
    reviews = Review.objects.all().order_by('-created_at')[:4]
    all_reviews_count = Review.objects.count()
    return render(request, 'bandsite/home.html', {'reviews': reviews, 'all_reviews_count': all_reviews_count})


def about(request):
    return render(request, 'bandsite/about.html')




def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cont creat cu succes!')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
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
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail(
                f'Mesaj de la {name}',
                message,
                email,
                ['trupe@site.com'],
            )
            return render(request, 'bandsite/contact_success.html')
    else:
        form = ContactForm()

    return render(request, 'bandsite/contact.html', {'form': form})


def submit_review(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        if name and rating and comment:
            Review.objects.create(name=name, rating=rating, comment=comment)
            messages.success(request, 'Recenzia ta a fost adăugată cu succes!')
            return redirect('home')
        else:
            messages.error(request, 'Te rugăm să completezi toate câmpurile!')
            return redirect('home')
    return HttpResponse("Invalid request method", status=400)


def load_more_reviews(request):
    reviews = Review.objects.all().order_by('-created_at')
    paginator = Paginator(reviews, 4)
    page = request.GET.get('page', 1)
    reviews_page = paginator.get_page(page)

    reviews_data = [
        {
            'name': review.name,
            'comment': review.comment,
            'rating': review.rating,
            'created_at': review.created_at.strftime('%d-%m-%Y'),
        }
        for review in reviews_page
    ]

    return JsonResponse({'reviews': reviews_data})
