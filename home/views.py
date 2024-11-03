from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView, CreateView, View
from django.contrib import messages

from .models import AboutModel, ServiceModel, ContactModel
from django.urls import reverse_lazy
from .forms import ContactModelForm

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
    form_class = ContactModelForm
    success_url = reverse_lazy('home:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = ServiceModel.objects.filter(is_available=True)

        return context

    def form_valid(self, form):
        form.save()
        # messages.success("Your message is well-received!")
        return redirect(self.success_url)

    def form_invalid(self, form):
        # messages.error()
        return redirect("home:about")

