from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

app_name = 'core'

urlpatterns = [
    #path('', views.WelcomeView, name='welcome'),
    path('', views.HomeView, name='home'),
    path('about', views.AboutView, name='about'),
    path('resume', views.ResumeView, name='resume'),
    path('portfolio', views.PortfolioView, name='portfolio'),
    path('services', views.ServicesView, name='services'),
    path('contact', views.ContactView, name='contact'),

    ]