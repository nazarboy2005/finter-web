from django.db import models

class AboutModel(models.Model):
    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.text[:20]}"

    class Meta:
        verbose_name = 'about'
        verbose_name_plural = 'abouts'