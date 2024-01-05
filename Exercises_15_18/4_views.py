# views.py

from django.shortcuts import render, redirect
from .forms import AutoForm

def add_auto(request):
    if request.method == 'POST':
        form = AutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # перенаправление на страницу "success" после успешного сохранения
    else:
        form = AutoForm()

    return render(request, 'add_auto.html', {'form': form})
