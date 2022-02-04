from django.http import HttpResponse
from django.shortcuts import render, redirect
from TaskManager.models import Tasks, Signup
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import mysql.connector
from operator import itemgetter

# Create your views here.
def home(request):
    return render(request, 'authentication/index.html')

def sessions(request):
        if request.POST.get('SignIn'):
            return render(request, 'authentication/signin.html')
        if request.POST.get('SignOut'):
            return render(request, 'authentication/signup.html')

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')  # OR username = request.POST['username']
        email = request.POST.get('email')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        '''
        register = Signup()
        register.Username = username
        register.Email = email
        register.First_Name = fname
        register.Last_Name = lname
        register.Password = pass1
        register.Confirm_Password = pass2

        register.save()
        messages.success(request, "Registeration successfull!")
        return redirect('signin')
        '''
        print(username, fname, lname)
        booluname = Signup.objects.filter(Username=username).exists()
        boolemail = Signup.objects.filter(Email=email).exists()
        if booluname == True or boolemail == True:
            if booluname == True and boolemail == True:
                messages.error(request, "Username and Email already exists!")
            elif booluname == True:
                messages.error(request, "Username already exists!")
            elif boolemail == True:
                messages.error(request, "Email already exists!")
            return render(request, 'authentication/index.html')
        elif len(pass1) < 8 :
            context = {
                'error' : "Password must be atleast 8 characters"
            }
            return render(request, 'authentication/index.html', context)
        elif pass1 != pass2:
            context = {
                'errornotmatch': "Password didn't match"
            }
            return render(request, 'authentication/index.html', context)
        else:
            sup = Signup(Username=username, First_Name=fname, Last_Name=lname, Email=email, Password=pass1,
                         Confirm_Password=pass2)
            sup.save()
            
            messages.success(request, "Registeration successfull!")
            return redirect('signin')


def signin(request):

    con1 = mysql.connector.connect(host="localhost", user="root", password="root", database="pythonDB")
    cursor1 = con1.cursor()
    con2 = mysql.connector.connect(host="localhost", user="root", password="root", database="pythonDB")
    cursor2 = con2.cursor()
    sqlcommand1 = "select Username from taskmanager_signup"
    sqlcommand2 = "select Password from taskmanager_signup"

    cursor1.execute(sqlcommand1)
    cursor2.execute(sqlcommand2)

    el = []
    pl = []

    for i in cursor1:
        el.append(i)

    for i in cursor2:
        pl.append(i)

    res1 = list(map(itemgetter(0),el))
    res2 = list(map(itemgetter(0),pl))


    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        i = 0
        k = len(res1)
        while i < k:
            print(res1[i])
            print(res2[i])
            if res1[i] == username and res2[i] == password:
                return render(request, 'tasks.html')
            i += 1
        else:
            messages.error(request, "Check username or password ")
            return redirect('signin')

    return render(request, 'authentication/signin.html')

    '''
        print(username)
        print(password)
        uname = Signup.objects.filter(Username=username,Password=password).exists()
        print(uname)
        if uname:
            obj = Signup()
            user = obj.authenticate(Username=username,Password=password)
            print(user)
            if user:4
                login(request,user)
                messages.success(request,"Login success!")
                return redirect('home')
            else:
                messages.error(request,"login failed!")
                return redirect('signin')
        else:
            messages.error(request,"login unattempt ")
            return redirect('signin')
    return render(request, 'authentication/signin.html')
    '''

def signout(request):
    logout(request)
    return redirect('signin')

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






