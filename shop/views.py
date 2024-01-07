from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm


# Create your views here.
def index(request):
    return render(request,'index.html')
def contact(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            messages.success(request, 'Your message was successfully submitted.')

            return redirect('/')



    return render(request, 'contact.html', {'form': form})


def shopping(request):
    return render(request,'shopping.html')