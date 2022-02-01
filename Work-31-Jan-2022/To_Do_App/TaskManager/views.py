from django.http import HttpResponse
from django.shortcuts import render
from TaskManager.models import Tasks
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'authentication/index.html')

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username') # OR username = request.POST['username']
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpsw = request.POST.get('cpsw')
    return render(request, 'authentication/signup.html')

def signin(request):
    return render(request, 'authentication/signin.html')

def signout(request):
    pass

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
        if request.POST.get('read'):
            return render(request, 'read.html')

def create(request):
    if request.method == "POST":
        if request.POST.get('create'):
            tname = request.POST.get('tname')
            tdesc = request.POST.get('tdesc')
            task = Tasks(TaskName=tname, TaskDescription=tdesc)
            task.save()
            #messages.success(request,"Task created!")
            messages.info(request, "Task created!")
            return render(request, 'create.html')
        if request.POST.get('back'):
            return render(request, 'tasks.html')

def read(request):
    if request.method == "POST":
        if request.POST.get('show'):
            data = Tasks.objects.all()
            if len(data) == 0:
                messages.error(request, "Tasks not exists!")
                return render(request, 'read.html')
            else:
                context = {
                    "TasksData" : data
                }
                #print(data)
                return render(request, 'read.html',context)
        if request.POST.get('read'):
                return render(request, 'readid.html')
        if request.POST.get('back'):
            return render(request, 'tasks.html')

def readid(request):
    if request.method == "POST":
        if request.POST.get('read'):
            try:
                tid = request.POST.get('taskid')
                #print(tid)
                singledata = Tasks.objects.get(pk=tid)
                #print(singledata)
                context = {
                    "task": singledata
                }
                print(context)
                return render(request, 'readid.html', context)
            except:
                messages.error(request, "ID not exists!")
                return render(request, 'readid.html')
        if request.POST.get('back'):
            return render(request, 'read.html')

def delete(request):
    if request.method == "POST":
        if request.POST.get('delete'):
            tid = request.POST.get('taskid')
            deletedata = Tasks.objects.filter(pk=tid).delete()
            print(deletedata)
            print(type(deletedata))
            if deletedata[0] == 0:
                messages.error(request, "ID not exists!")
            else:
                messages.info(request, "Task deleted!")
            return render(request, 'delete.html')
        if request.POST.get('deleteall'):
            deleteall = Tasks.objects.all()
            if len(deleteall) == 0:
                messages.error(request, "Tasks not exists!")
            else:
                deleteall.delete()
                messages.info(request, "All Tasks deleted!")
            return render(request, 'delete.html')
        if request.POST.get('back'):
            return render(request, 'tasks.html')

def update(request):
    if request.method == "POST":
        if request.POST.get('update'):
            tid = request.POST.get('taskid')
            tname = request.POST.get('tname')
            tdesc = request.POST.get('tdesc')
            result = Tasks.objects.filter(pk=tid).update(TaskName=tname, TaskDescription=tdesc)
            # print(result)
            if result == 1:
                messages.info(request, "Task updated!")
            else:
                messages.error(request, "Tasks not exists!")
            return render(request, 'update.html')
        if request.POST.get('back'):
            return render(request, 'tasks.html')






