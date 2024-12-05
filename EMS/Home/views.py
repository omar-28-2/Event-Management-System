from django.shortcuts import render ,redirect
import re
from .models import ContactSubmission

def index(request):
    return render(request, 'Home/index.html')

def about(request):
    return render(request, 'Home/about.html')

def contact(request):
    return render(request, 'Home/contact.html')

def contactForm(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        message = request.POST.get("message", "").strip()

        if not name.isalpha() or len(name) < 3:
            return render(request, "Home/contact.html", {"error": "Please enter a valid name."})
        elif not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
            return render(request, "Home/contact.html", {"error": "Please enter a valid email address."})
        elif len(message) < 10:
             return render(request, "Home/contact.html", {"error": "Please enter a message with at least 10 characters."})
        else:
            ContactSubmission.objects.create(name=name, email=email, message=message)
            
            return render(request, "Home/contact.html", {"success": True})
        
    return render(request, "Home/contact.html")

def signup(request):
    return render(request, 'Home/signUp.html')

def login(request):
    return render(request, 'Home/login.html')
