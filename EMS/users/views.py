from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate,login
import re


def signup(request):
    if request.method == "POST":
        email = request.POST.get('email')
        username = request.POST.get('username')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        user_type = request.POST.get('user_type')

        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email): # Assumes email should be in this format
            messages.error(request, "Invalid email format!")
            return render(request, 'users/signup.html')
        
        if not re.match(r'^\d{11}$', phone_number):  # Assumes phone number should be 11 digits
            messages.error(request, "Phone number must be 11 digits!")
            return render(request, 'users/signup.html')
        
        if not re.match(r'^[a-zA-Z0-9_]+$', username): ## check that username must be in this format
            messages.error(request, "Username can only contain letters, numbers, and underscores.")
            return render(request, 'users/signup.html')
        
        # Validate password strength
        if not re.fullmatch(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password):
            messages.error(
                request, 
                "Password must contain at least 8 characters, including uppercase, lowercase, number, and a symbol."
            )
            return render(request, 'users/signup.html')
        
        # Validate passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return render(request, 'users/signup.html')
        
        if len(username) < 5 or len(username) > 15: ## check that the username must be between [5:15] length
           messages.error(request, "Username must be between 5 and 15 characters long.")
           return render(request, 'users/signup.html')

        # Check if user with email or username or phone_number already exists
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return render(request, 'users/signup.html')
        
        if CustomUser.objects.filter(phone_number=phone_number).exists():
            messages.error(request, "phone_number already exists!")
            return render(request, 'users/signup.html')
        
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return render(request, 'users/signup.html')

        user = CustomUser(email=email,username=username,phone_number=phone_number,user_type=user_type,is_active=True)
        user.set_password(password)  # Hash the password
        user.save()

        messages.success(request, "Signup successful!")
        return redirect("login")

    return render(request, 'users/signup.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print(f"i am here for logging") ## Debugging line
            return redirect('index')
        else:
            messages.error(request, "Invalid email or password. Please try again.")
            print(f"i am here for not logging") ## Debugging line 
            return redirect("login")

    return render(request, "users/login.html")


    
