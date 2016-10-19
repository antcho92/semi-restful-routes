from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import Pet

# Create your views here.
def index(request):
    context = {
        'pets': Pet.objects.all()
    }
    return render(request, 'pets/index.html', context)

def new(request):
    return render(request, 'pets/new.html')

def create(request):
    if request.method == 'POST':
        validation = Pet.objects.add_pet(request.POST)
        if validation[0]:
            return redirect(reverse('pets:index'))
        else:
            for error in validation[1]:
                messages.error(request, error)
    return redirect(index)

def show(request, id):
    print(id)
    print("show")
    context = {
        'pet': Pet.objects.get(id=id)
    }
    print(context['pet'])
    return render(request, 'pets/show.html', context)
def edit(request, id):
    print(id)
    print("edit")
    context = {
        'pet': Pet.objects.get(id=id)
    }
    return render(request, 'pets/edit.html', context)
def update(request, id):
    print("updating a pet")
    if request.method == 'POST':
        validation = Pet.objects.edit_pet(request.POST, id)
        return redirect(reverse('pets:index'))
    return
def destroy(request, id):
    print("destroying pet")
    Pet.objects.get(id=id).delete()
    return redirect('/pets')
