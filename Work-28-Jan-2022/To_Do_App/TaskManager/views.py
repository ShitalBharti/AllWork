from django.http import HttpResponse
from django.shortcuts import render
from TaskManager.models import Tasks
from django.contrib import messages

# Create your views here.
def show(request):
    #return HttpResponse("this is homepage")
    return render(request, 'tasks.html')

def display(request):
    if request.method == "POST":
        if request.POST.get('create'):
           return render(request, 'create.html')
        if request.POST.get('delete'):
            return render(request, 'delete.html')
        if request.POST.get('update'):
            return render(request, 'update.html')
        if request.POST.get('readid'):
            return render(request, 'readid.html')
        if request.POST.get('readall'):
            return render(request, 'readall.html')

def create(request):
    if request.method == "POST":
        if request.POST.get('create'):
            tname = request.POST.get('tname')
            tdesc = request.POST.get('tdesc')
            task = Tasks(TaskName=tname, TaskDescription=tdesc)
            task.save()
            messages.success(request,"Task created!")
            return render(request, 'tasks.html')
        if request.POST.get('back'):
            return render(request, 'tasks.html')

def readall(request):
    if request.method == "POST":
        if request.POST.get('show'):
            data = Tasks.objects.all()
            context = {
                "TasksData" : data
            }
            #print(data)
            return render(request, 'readall.html',context)
        if request.POST.get('back'):
            return render(request, 'tasks.html')

def readid(request):
    if request.method == "POST":
        tid = request.POST.get('taskid')
        singledata = Tasks.objects.get(pk=tid)
        print(singledata)
        context = {
            "TasksData": singledata
        }
        print(context)
        return render(request, 'readid.html', context)
    '''except:
            messages.error(request, "ID not exists!")
            return render(request, 'tasks.html')'''




