from django.shortcuts import render


def handler404(request, exception):
    return render(request=request, template_name='error-404.html')


def handler500(request):
    return render(request=request, template_name='error-500.html')
