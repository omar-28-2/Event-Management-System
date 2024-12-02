from django.shortcuts import render

def index(request):
    return render(request, 'Home/index.html')

def about(request):
    return render(request, 'Home/about.html')

def contact(request):
    return render(request, 'Home/contact.html')

