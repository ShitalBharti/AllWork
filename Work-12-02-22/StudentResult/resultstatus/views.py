from django.shortcuts import render, redirect
from resultstatus.models import StudentResultData
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'index.html')

def insertMarks(request):
    if request.method == "POST":
        if request.POST.get('insert'):
            sname = request.POST.get('sname')
            maths = request.POST.get('maths')
            history = request.POST.get('history')
            geography = request.POST.get('geography')
            english = request.POST.get('english')
            civics = request.POST.get('civics')
            economics = request.POST.get('economics')
            new_student = StudentResultData(StudentName=sname, Maths=float(maths), History=float(history), Geography=float(geography),
                                            English=float(english), Civics=float(civics), Economics=float(economics))
            new_student = findresult(new_student)
            new_student.save()
            messages.info(request, "Student Result Inserted Successfully!!")
            #return redirect(request, 'insert.html')
    return render(request, 'insert.html')

def findresult(new_student):
    markdicts1 = {}

    markdicts1.update({'Maths': new_student.Maths})
    markdicts1.update({'History': new_student.History})
    markdicts1.update({'English': new_student.English})
    markdicts1.update({'Geography': new_student.Geography})
    markdicts1.update({'Civics': new_student.Civics})
    markdicts1.update({'Economics': new_student.Economics})
    marks1 = markdicts1.values()

    total_per = sum(marks1) / 6

    count1 = 0
    for i in marks1:
        if i >= 95.0:
            count1 = count1 + 1

    count2 = 0
    subname = []
    for i, j in markdicts1.items():
        if j <= 75.0:
            sname = i
            subname.append(sname)
            count2 = count2 + 1

    if total_per >= 90:
        if count1 >= 3:
            new_student.Status = "Gold medal and distinciton"
            new_student.chance_given = 0
            return new_student
        else:
            new_student.Status = "Distinction"
            new_student.Chance_Given = 0
            return new_student

    if 75.0 <= total_per < 90.0:
        new_student.Status = "Average"
        new_student.Chance_Given = 0
        return new_student

    if total_per < 75.0:
        if count2 > 3:
            new_student.Status = "Failed"
            new_student.Chance_Given = 0
            return new_student
        else:
            new_student.Chance_Given = 0
            new_student.Status = "Failed"
            return new_student

def displayMarks(request):
    if request.method == "POST":
        if request.POST.get('show'):
            data = StudentResultData.objects.all()
            if len(data) == 0:
                messages.error(request, "Data not present!")
                return render(request, 'displayAll.html')
            else:
                context = {
                    "ResultData": data
                }
                return render(request, 'displayAll.html', context)
    return render(request, 'displayAll.html')

def displayMarksID(request):
    if request.method == "POST":
        if request.POST.get('read'):
            try:
                sid = request.POST.get('sid')
                singledata = StudentResultData.objects.get(pk=sid)
                context = {
                    "result": singledata
                }
                print(context)
                return render(request, 'displayone.html', context)
            except:
                messages.error(request, "Student ID not exists!")
                return render(request, 'displayone.html')
    return render(request, 'displayone.html')


def deleteRecord(request):
    if request.method == "POST":
        if request.POST.get('delete'):
            sid = request.POST.get('sid')
            deletedata = StudentResultData.objects.filter(pk=sid).delete()
            if deletedata[0] == 0:
                messages.error(request, "Student ID not exists!")
            else:
                messages.info(request, "Record deleted!")
            return render(request, 'deleteone.html')
    return render(request, 'deleteone.html')


def updateMarks(request):
    if request.method == "POST":
        if request.POST.get('update'):
            sid = request.POST.get('sid')
            if StudentResultData.objects.filter(pk=sid):
                fetch_data = StudentResultData.objects.get(pk=sid)
                if fetch_data.Chance_Given < 4 and fetch_data.Status == "Failed":
                    if fetch_data.Maths < 75:
                        fetch_data.Maths = float(request.POST.get('maths'))
                    if fetch_data.History < 75:
                        fetch_data.History = float(request.POST.get('history'))
                    if fetch_data.Geography < 75:
                        fetch_data.Geography = float(request.POST.get('geography'))
                    if fetch_data.English < 75:
                        fetch_data.English = float(request.POST.get('english'))
                    if fetch_data.Civics < 75:
                        fetch_data.Civics = float(request.POST.get('civics'))
                    if fetch_data.Economics < 75:
                        fetch_data.Economics = float(request.POST.get('economics'))
                    markdicts1 = {}

                    markdicts1.update({'Maths': fetch_data.Maths})
                    markdicts1.update({'History': fetch_data.History})
                    markdicts1.update({'English': fetch_data.English})
                    markdicts1.update({'Geography': fetch_data.Geography})
                    markdicts1.update({'Civics': fetch_data.Civics})
                    markdicts1.update({'Economics': fetch_data.Economics})
                    marks1 = markdicts1.values()

                    total_per = sum(marks1) / 6

                    if total_per < 75.0:
                        fetch_data.Chance_Given += 1
                        fetch_data.Status = "Failed"
                    else:
                        fetch_data.Chance_Given += 1
                        fetch_data.Status = "Passed"

                    fetch_data.save()
                    messages.info(request, "Student Result Updated Successfully!!")
                    return render(request, 'updateone.html')
                else:
                    messages.error(request, "Student not allow to update marks!")
                    return render(request, 'updateone.html')

    return render(request, 'updateone.html')

#def uploadCSVFile(request):





