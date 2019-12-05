from django.shortcuts import render
from .forms import town_form

def home(request):
    return render(request, 'home.html')

def town_trip(request):
    if request.method == 'POST':
        filled_form = town_form(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            note = 'Your Transport request has been sent to %s for approval' %(filled_form.cleaned_data['trans_officer'])
            new_form = town_form()
            return render(request, 'town_trip.html', {'town_form':new_form, 'note':note})
    else:
            trip = town_form()
            note = 'Fill in the right details'
            return render(request, 'town_trip.html', {'town_form':trip, 'note':note})
