from django.shortcuts import render
from django.views.generic import ListView, TemplateView, CreateView, View
from .models import AboutModel, ServiceModel
from django.urls import reverse_lazy

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        about = AboutModel.objects.filter(is_selected=True).order_by('-selected_at').first()
        context['text_about'] = about.text[:1000]
        context['image_about'] = about.image

        services = ServiceModel.objects.filter(is_available=True).order_by('-updated_at')
        context['services'] = services

        return context


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        about = AboutModel.objects.filter(is_selected=True).order_by('-selected_at').first()
        print(about)
        context['text_about'] = about.text
        context['image_about'] = about.image
        return context



class ServiceView(TemplateView):
    template_name = 'service.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        services = ServiceModel.objects.filter(is_available=True).order_by('-updated_at')
        context['services'] = services
        return context


class TeamView(TemplateView):
    template_name = 'team.html'




class ContactView(CreateView):
    template_name = 'contact.html'
    success_url = reverse_lazy('home:home')
    # model = ContactModel
    # form_class = ContactModelForm
