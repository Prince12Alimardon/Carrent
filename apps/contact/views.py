from django.shortcuts import render
from .models import Contact
from .forms import ContactForm


# Create your views here.

def contact_page(req):
    form = ContactForm(req.POST or None)
    if form.is_valid():
        form.save()
    ctx = {
        'form': form
    }
    return render(req, 'contact.html', ctx)
