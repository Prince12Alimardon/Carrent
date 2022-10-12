from django.shortcuts import render, redirect
from .models import Car
from .forms import RentForm, Rent
from ..blog.models import How_it_works
from django.db.models import Q


# Create your views here.

def home_page(req):
    form = RentForm(req.POST or None)
    wyf = form.data.get('wyf')
    print(wyf)
    wyg = form.data.get('wyg')
    print(wyg)
    j_d = form.data.get('jurney_d')
    print(j_d)
    r_d = form.data.get('return_d')
    print(r_d)
    count = Car.objects.all().count()
    hiw = How_it_works.objects.all()
    if wyf and wyg and j_d and r_d:
        cars = []
        print("ishladimi")
        rents = Rent.objects.filter(Q(wyf__iexact=wyf) and Q(wyg__iexact=wyg) and Q(jurney_d__exact=j_d) and Q(
            return_d__exact=r_d)).all()
        for i in rents:
            cars.append(i.car)
        ctx = {
            'cars': cars,
        }
        return render(req, 'cars.html', ctx)
    ctx = {
        'form': form,
        'count': count,
        'hiws': hiw,
    }
    return render(req, 'index.html', ctx)


def car(req):
    cars = Car.objects.all().order_by('-id')[:6]
    hiw = How_it_works.objects.all()
    ctx = {
        'cars': cars,
        'l': [0, 1, 2, 3, 4],
        'hiws': hiw
    }
    return render(req, 'cars.html', ctx)


def rent(req, pk):
    form = RentForm(req.POST or None)
    obj = Car.objects.get(id=pk)

    if form.is_valid():
        # print('ishladinmi?')
        abc = form.save(commit=False)
        abc.car = obj
        abc.save()
        # print('sev')
    ctx = {
        'form': form
    }
    return render(req, 'rent.html', ctx)
