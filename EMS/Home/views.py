from django.shortcuts import render

def index(request):
    return render(request, 'Home/index.html')

def about(request):
    return render(request, 'Home/about.html')

def contact(request):
    return render(request, 'Home/contact.html')

def signup(request):
    return render(request, 'Home/signUp.html')

def login(request):
    return render(request, 'Home/login.html')
