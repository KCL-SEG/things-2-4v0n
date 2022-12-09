from django.shortcuts import render
from things.forms import ThingForm

def home(request):
    if request.method == 'GET':
        form = ThingForm()
        return render(request, 'home.html', {'form': form})
