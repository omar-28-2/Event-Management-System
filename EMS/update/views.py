from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile
import re


def validate_password(password):
    """Function to validate the new password."""
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    if not re.search(r'[A-Z]', password):
        return "Password must contain at least one uppercase letter."
    if not re.search(r'[a-z]', password):
        return "Password must contain at least one lowercase letter."
    if not re.search(r'[0-9]', password):
        return "Password must contain at least one number."
    if not re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
        return "Password must contain at least one special character."
    return None


@login_required
def update(request):
    """View for updating phone number and password for the logged-in user."""
    if request.method == "POST":
        # Capture the data from the form
        update_choice = request.POST.get("update_choice")  # "1", "2", or "3"
        new_phone = request.POST.get("new_phone", "").strip()
        new_password = request.POST.get("new_password", "").strip()
        confirm_password = request.POST.get("confirm_password", "").strip()

        # Check if the user selected phone number, password, or both
        if update_choice in ["1", "3"]:  # Phone number update
            if new_phone:
                # Validate phone number length and uniqueness
                if not new_phone.isdigit() or len(new_phone) != 11:
                    messages.error(request, "Phone number must be exactly 11 digits.")
                    return redirect("update")
                if Profile.objects.filter(phone_number=new_phone).exists():
                    messages.error(request, "This phone number is already in use.")
                    return redirect("update")
                
                # Update the phone number in the Profile model
                request.user.phone_number = new_phone  # Update the phone number
                request.user.save()  # Save changes
            else:
                messages.error(request, "Please enter a valid phone number.")
                return redirect("update")


        if update_choice in ["2", "3"]:  # Password update
            if new_password and new_password == confirm_password:
                # Validate the new password
                password_error = validate_password(new_password)
                if password_error:
                    messages.error(request, password_error)
                    return redirect("update")
                # Update the password
                request.user.set_password(new_password)
                request.user.save()
                messages.success(request, "Password updated successfully! Please log in again.")
                return redirect("login")  # Redirect to login after password change
            else:
                messages.error(request, "Passwords do not match.")
                return redirect("update")

        messages.success(request, "Your information has been updated successfully!")
        return redirect("update")  # Redirect after successful update

    # Render the form for GET request
    return render(request, "update/update.html")
