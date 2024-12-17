from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate,login


def signup(request):
    if request.method == "POST":
        email = request.POST.get('email')
        username = request.POST.get('username')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        user_type = request.POST.get('user_type')

        # Validate passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return render(request, 'users/signup.html')

        # Check if user with email or username already exists
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return render(request, 'users/signup.html')
        
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return render(request, 'users/signup.html')

        # Save the user
        # user = CustomUser(email=email, username=username,password=password, phone_number=phone_number, user_type=user_type, is_active=True)
        # user.save()
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


    
