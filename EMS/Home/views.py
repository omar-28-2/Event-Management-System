from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ContactMessage

def index(request):
    return render(request, 'Home/index.html')

def about(request):
    return render(request, 'Home/about.html')

def contact(request):
    return render(request, 'Home/contact.html')


def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save data to the database
        ContactMessage.objects.create(name=name, email=email, message=message)

        # Return a success message or redirect
        return render(request, 'contact_success.html')  # Create this template for success
    return render(request, 'contact.html')  # Replace with your contact page template