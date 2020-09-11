from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from .models import Item


def products(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'products.html', context)


def checkout(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'checkout.html', context)


def home(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'home.html', context)
