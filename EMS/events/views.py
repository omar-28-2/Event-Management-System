from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event

@login_required
def events_list(request):
    return render(request, 'events/events_list.html')

@login_required
def request_form(request):
    return render(request, 'events/event_form.html', {'vendor': request.user})

@login_required
def vendor_event_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        date = request.POST.get('date')
        location = request.POST.get('location')
        number_of_seats = request.POST.get('number_of_seats')
        price = request.POST.get('price') 

        # Validate form data
        if not name or not description or not date or not location or not number_of_seats:
            messages.error(request, "All fields must be filled in.")
            return redirect('events_list')

        # Check date format if needed
        from datetime import datetime
        try:
            date = datetime.strptime(date, "%Y-%m-%dT%H:%M")
        except ValueError:
            messages.error(request, "Invalid date format.")
            return redirect('events_list')

        # Save the event in the Event model
        event = Event.objects.create(
            name=name,
            description=description,
            date=date,
            location=location,
            vendor=request.user,
            number_of_seats=number_of_seats,
            price=price 
        )

        # Debugging: Confirm if the event is saved
        print(f"Event saved: {event}")

        # Display success message
        messages.success(request, "Your event has been submitted and is pending approval.")
        return redirect('events_list')

