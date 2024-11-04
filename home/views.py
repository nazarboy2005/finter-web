from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView, View
from django.contrib import messages

from conf import settings
from .models import AboutModel, ServiceModel, StaffModel, TestimonialModel, SubscribersModel
from .forms import ContactModelForm
from django.core.mail import send_mail
from django.http import HttpResponse


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        about = AboutModel.objects.filter(is_selected=True).order_by('-selected_at').first()
        context['text_about'] = about.text[:1000]
        context['image_about'] = about.image

        services = ServiceModel.objects.filter(is_available=True).order_by('-updated_at')
        context['services'] = services

        context['workers'] = StaffModel.objects.filter(is_working=True, web_display=True)
        context['testimonials'] = TestimonialModel.objects.filter(is_displayed=True)

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['workers'] = StaffModel.objects.filter(is_working=True, web_display=True)

        return context


class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = ServiceModel.objects.filter(is_available=True)

        return context

    def form_valid(self, form):
        form.save()
        messages.success(self.request, message="Your message is well-received!")

        return redirect("home:contact")

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return redirect("home:contact")


def send_email(email):
    with open('subscribe-email.txt', 'r') as file:
        text = file.read()
        try:
            send_mail(message=text, subject="Welcome to FINTER! You've Successfully Subscribed ",
                      recipient_list=[email],
                      from_email=settings.EMAIL_HOST_USER)

            return True
        except ConnectionError as e:
            return False


def subscribe_view(request):
    subscriber_email = request.POST.get('subscriber_email')
    next_url = request.GET.get('next', '/')
    print(next_url)
    if subscriber_email and send_email(subscriber_email):
        SubscribersModel.objects.create(
            email=subscriber_email
        )
        return redirect(next_url)
    else:
        return HttpResponse("Subscription Failed")
