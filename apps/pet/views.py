from django.shortcuts import render, redirect
# from django.http import HttpResponse

from .forms import PetForm


def index(request):
    return render(request, "pet/index.html")


def pet_create(request):
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('pet:index')
    else:
        form = PetForm()

    return render(request, 'pet/pet_create.html', {'form': form})
