# bandsite/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('about/', views.about, name='about'),  # About page
    path('gallery/', views.gallery, name='gallery'),  # Gallery page
    path('login/', LoginView.as_view(template_name='bandsite/login.html'), name='login'),  # Login page
    path('logout/', LogoutView.as_view(), name='logout'),  # Logout page
    path('register/', views.register, name='register'),  # Register page
    path('members/', views.members, name='members'),  # Members page
    path('albums/', views.albums, name='albums'),  # Albums page
    path('concerts/', views.concerts, name='concerts'),  # Concerts page
    path('contact/', views.contact_view, name='contact'),  # Contact page
    path('submit-review/', views.submit_review, name='submit_review'),
    path('submit-review/', views.submit_review, name='submit_review'),
    path('load_more_reviews/', views.load_more_reviews, name='load_more_reviews'),
]
