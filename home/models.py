from django.db import models
from django.core.exceptions import ValidationError

class AboutModel(models.Model):
    text = models.TextField()
    is_selected = models.BooleanField(default=False)
    image = models.ImageField(upload_to='about-images', null=True)

    selected_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.text[:20]}"

    class Meta:
        verbose_name = 'about'
        verbose_name_plural = 'abouts'


def validate_image_png(image):
    if not image.name.endswith('.png'):
        raise ValidationError("Only PNG images are allowed.")


class ServiceModel(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='service-images', null=True, validators=[validate_image_png])

    is_available = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class ContactModel(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=14)
    email = models.EmailField()
    message = models.TextField()

    is_answered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    service = models.ForeignKey(ServiceModel, on_delete=models.DO_NOTHING, limit_choices_to={'is_available' : True})

    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'


class StaffModel(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    image = models.ImageField(upload_to='staff-images', null=False)
    is_working = models.BooleanField(default=True)
    experience = models.SmallIntegerField()
    web_display = models.BooleanField(default=False)


    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.position}"

    class Meta:
        verbose_name = 'worker'
        verbose_name_plural = 'workers'

class TestimonialModel(models.Model):
    name = models.CharField(max_length=25)
    message = models.TextField()
    image = models.ImageField(upload_to='testimonial-image')
    position = models.CharField(max_length=25)

    is_displayed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'