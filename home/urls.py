from django.urls import path
from .views import HomeView, AboutView, ContactView, ServiceView, TeamView

app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('services/', ServiceView.as_view(), name='services'),
    path('team/', TeamView.as_view(), name='team'),
]
