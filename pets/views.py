from django.shortcuts import render

from django.shortcuts import render

def index(request):
    return render(request, 'pets/index.html')

def contact(request):
    return render(request, 'pets/contact.html')

def about(request):
    return render(request, 'pets/about.html')

