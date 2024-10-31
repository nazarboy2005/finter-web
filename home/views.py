from django.shortcuts import render
from django.views.generic import ListView, TemplateView, CreateView

class HomeView(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class ServiceView(TemplateView):
    template_name = 'service.html'

class TeamView(TemplateView):
    template_name = 'team.html'


class HomeView(TemplateView):
    template_name = 'index.html'