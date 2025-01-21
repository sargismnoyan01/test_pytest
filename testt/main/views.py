from django.shortcuts import redirect, render
from .models import *
from .forms import *



def HomePage(request):
    userclass = UserClass.objects.all()
    form = UserFrom()
    if request.method == 'POST':
        form = UserFrom(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('/')

    return render(request, 'index.html', {'userclass': userclass, 'form': form})

