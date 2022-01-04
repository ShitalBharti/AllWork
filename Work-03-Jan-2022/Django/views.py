from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response
# request handler
# action

def say_hello(request):
   # return HttpResponse('Hello World') # to return message
   # return render(request, 'hello.html')    # to return html page
   # return render(request, 'hello.html', {'name':'Shital'})   # to display name on html page
    return render(request, 'hello.html')