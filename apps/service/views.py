from django.shortcuts import render
from .models import Service
from ..blog.models import How_it_works


# Create your views here.
def service(req):
    services = Service.objects.all().order_by('-id')[:6]
    hiw = How_it_works.objects.all()
    ctx = {
        'services': services,
        'hiws': hiw
    }
    return render(req, 'services.html', ctx)
