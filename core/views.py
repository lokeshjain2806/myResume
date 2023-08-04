from django.shortcuts import render
from .forms import contact1
# from .models import con


# Create your views here.
def home(request):
    context = {'home': 'active'}
    return render(request, 'core/home.html', context)

def contact(request):
    if request.method == 'POST':
        form = contact1(request.POST)
        if form.is_valid():
            form.save()
            return home(request)
    else:
        form = contact1()
    context = {'contact': 'active','form': form }
    return render(request, 'core/contact.html', context)
