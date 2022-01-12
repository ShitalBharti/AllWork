from django.shortcuts import render, redirect, get_object_or_404
from requests import post

from .models import Employee
from .forms import EmployeeData
from django.views.generic import ListView, DetailView

# Create your views here.
class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'empdata'

    def get_queryset(self):
        return Employee.objects.all()



def create(request):
    if request.method == 'POST':
        form = EmployeeData(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = EmployeeData()

    return render(request,'create.html',{'form': form})

d    
