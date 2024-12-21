from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import re


def signup(request):
    if request.user.is_authenticated:  # Redirect logged-in users away from the signup page
        return redirect('index')
    
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
    
    if request.user.is_authenticated:  # Redirect logged-in users away from the login page
        return redirect('index')
    
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


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "You have successfully logged out.")
        return redirect('index')
    return redirect('login')  # Redirect if not logged in


@login_required
def update(request):
    if request.method == "POST":
        user = request.user  # Get the currently logged-in user
        update_choice = request.POST.get('update_choice')

        # Handle phone number update
        if update_choice in ['1', '3']:  # '1' for phone only, '3' for both
            new_phone = request.POST.get('new_phone')
            if not new_phone:
                messages.error(request, "Phone number cannot be empty!")
                return redirect('update')
            if not re.match(r'^\d{11}$', new_phone):  # Assumes phone number should be 11 digits
                messages.error(request, "Phone number must be 11 digits!")
                return redirect('update')
            if CustomUser.objects.filter(phone_number=new_phone).exclude(id=user.id).exists():
                messages.error(request, "Phone number already exists!")
                return redirect('update')
            user.phone_number = new_phone

        # Handle password update
        if update_choice in ['2', '3']:  # '2' for password only, '3' for both
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')
            if not new_password or not confirm_password:
                messages.error(request, "Password fields cannot be empty!")
                return redirect('update')
            if new_password != confirm_password:
                messages.error(request, "Passwords do not match!")
                return redirect('update')
            # Validate password strength
            if not re.fullmatch(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', new_password):
                messages.error(
                    request,
                    "Password must contain at least 8 characters, including uppercase, lowercase, number, and a symbol."
                )
                return redirect('update')
            user.set_password(new_password)  # Hash and set the new password

        # Save the updated user object
        user.save()
        # Debugging prints
        username = user.username  # Use user.username for the current username
        password = new_password if update_choice in ['2', '3'] else None
        phone = new_phone if update_choice in ['1', '3'] else None
        print(f"Debugging Info - Username: {username}, New Password: {password}, New Phone: {phone}")
        messages.success(request, "Profile updated successfully!")
        return redirect('update')  # Redirect to the update page or any other page

    return render(request, 'users/update_profile.html')
