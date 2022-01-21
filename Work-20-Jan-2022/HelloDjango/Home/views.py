from django.shortcuts import render,HttpResponse
from datetime import datetime
from Home.models import Contact
from django.contrib import messages

# render: use to render to templates
# return: use to render to string
# context: It is python dictionary, use to send variables in html page

# Create your views here.
def index(request):
    # return HttpResponse("this is homepage")
    context = {
        'variable': 'this is sent'
    }
    return render(request, 'index.html', context)

def about(request):
    # return HttpResponse("this is about")
    return render(request, 'about.html')

def services(request):
    # return HttpResponse("this is service")
    return render(request, 'services.html')

def contact(request):
    # return HttpResponse("this is contact")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name = name, email = email,phone = phone, desc = desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your data is sent!')
    return render(request, 'contact.html')