from django.shortcuts import render
from . import models
# Create your views here.
def contact(request):
    if request.method == 'POST':
        print("This is post")
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        print(name,email,phone)
        ins = models.Contact(name = name, phone = phone, email = email)
        ins.save()
        print("Data is written in db")

    return render(request,'form.html')