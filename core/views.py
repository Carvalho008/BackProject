from django.shortcuts import render
from .forms import ClienteForm
from .models import Cliente

def Index(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            form = ClienteForm()
    else:
        form = ClienteForm()
    return render(request, 'index.html', {'form': form})