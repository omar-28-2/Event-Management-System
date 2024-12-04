from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import SignUpForm

def index(request):
    return render(request, 'Home/index.html')

def about(request):
    return render(request, 'Home/about.html')

def contact(request):
    return render(request, 'Home/contact.html')

# Sign Up View
def signup(request):
    return render(request, 'Home/signup.html')

# Login View
def login(request):
    return render(request, 'Home/login.html')



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Create user
            login(request, user)  # Log the user in
            return redirect('home')  # Redirect to the homepage (or a success page)
    else:
        form = SignUpForm()
    
    return render(request, 'Home/signup.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirect to a success page
    else:
        form = AuthenticationForm()
    return render(request, 'Home/login.html', {'form': form})
