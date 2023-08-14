from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from datetime import datetime
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "variable":"HELLO",
        "variable2": "HI"
    }
    return render(request, "index.html", context)
    # return HttpResponse("This is homepage")

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        desc = request.POST.get("desc")
        contact = Contact(name = name, phone = phone, email = email, desc = desc, date = datetime.today())
        contact.save()
        messages.success(request, "Your form is submitted!")
        return redirect('contact')
    return render(request, "contact.html")
    
