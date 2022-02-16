from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer

# Create your views here.

# Model object - Single Student Data

def student_detail(request):
    stu = Student.objects.get(id=2)
    print(stu)
    serializer = StudentSerializer(stu)
    print(serializer)
    json_data = JSONRenderer().render(serializer.data)
    print(json_data)
    return HttpResponse(json_data, content_type='application/json')

def student_detail1(request,pk):
    stu = Student.objects.get(id=pk)
    print(stu)
    serializer = StudentSerializer(stu)
    print(serializer)
    json_data = JSONRenderer().render(serializer.data)
    print(json_data)
    return HttpResponse(json_data, content_type='application/json')

def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    json_data = JSONRenderer().render(serializer.data)
    #return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data, safe=False)


