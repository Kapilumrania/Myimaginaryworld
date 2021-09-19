from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):

    #messages.success(request, "Yo")

    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
    #return HttpResponse("this is about page")
def services(request):
    return render(request, 'services.html')
    #return HttpResponse("this is services page")
def sciencefiction(request):
    return render(request, 'sciencefiction.html')
def fantasy(request):
    return render(request, 'fantasy.html')
def horror(request):
    return render(request, 'horror.html')


def contact(request):
    if request.method == "POST":
        name =request.POST.get('name')
        email =request.POST.get('email')
        desc =request.POST.get('desc')
        contact = Contact(name=name, email=email, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'message sent!.')
        

    return render(request, 'contact.html')
    #return HttpResponse("this is contact page")