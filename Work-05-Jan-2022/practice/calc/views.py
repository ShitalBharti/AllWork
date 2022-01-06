from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# def home(request):
  #  return HttpResponse("Hello World")

def home(request):
   return render(request, 'home.html')

def home(request):
   return render(request, 'home.html', {'name':'Shital'})

def home(request):
   return render(request, 'home.html', {'salary':40000})

'''
# to fetch data
def add(request):
   val1 = int(request.GET['num1'])
   val2 = int(request.GET['num2'])
   res = val1 + val2
   return render(request, 'result.html', {'result':res})
'''

# to post data
def add(request):
   val1 = int(request.POST['num1'])
   val2 = int(request.POST['num2'])
   res = val1 + val2
   return render(request, 'result.html', {'result':res})
