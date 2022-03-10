from django.shortcuts import render

# Create your views here.


def home(request):
    context = {}
    return render(request, 'apps/home.html', context)


def about(request):
    context = {}
    return render(request, 'general/about.html', context)


def contact(request):
    return render(request, 'general/contact.html')
