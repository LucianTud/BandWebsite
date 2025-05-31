# bandsite/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('login/', LoginView.as_view(template_name='bandsite/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('members/', views.members, name='members'),
    path('albums/', views.albums, name='albums'),
    path('concerts/', views.concerts, name='concerts'),
    path('contact/', views.contact_view, name='contact'),
    path('submit-review/', views.submit_review, name='submit_review'),
    path('load_more_reviews/', views.load_more_reviews, name='load_more_reviews'),
    path('galerie/adauga/', views.add_media, name='add_media'),
    path('delete_media/<int:media_id>/', views.delete_media, name='delete_media'),
    path('logout/', views.logout_view, name='logout'),
]
