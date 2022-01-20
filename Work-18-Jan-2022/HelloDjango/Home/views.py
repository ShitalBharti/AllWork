from django.shortcuts import render,HttpResponse

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
    return HttpResponse("this is about")

def services(request):
    return HttpResponse("this is service")

def contact(request):
    return HttpResponse("this is contact")