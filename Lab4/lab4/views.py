from django.shortcuts import render
from lab4.models import IceCream
from lab4.models import IceCreamShop


def index(request):
    return render(request, 'index.html')


def ice_cream_data(request):
    return render(request, 'ice_cream/index.html', {'data': {
        'ice_creams': IceCream.objects.all(),
    }})


def ice_cream_show(request, code):
    return render(request, 'ice_cream/show.html', {'data': {
        'ice_cream': IceCream.objects.filter(id=code)[0],
    }})


def shop_data(request):
    return render(request, 'shop/index.html', {'data': {
        'shops': IceCreamShop.objects.all(),
    }})
