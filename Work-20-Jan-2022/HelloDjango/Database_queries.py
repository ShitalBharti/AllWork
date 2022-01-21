'''
1. Go to terminal or command prompt type: python manage.py shell
2. Type, from appname.models import modelname
        e.g from Home.models import Contact
3. Type, Contact.objects.all()
    It will give query set i.e no of rows
4. To fetch particular data type: Contact.objects.all()[1].name ([1] represents 1st row)
5. To filter search,  Contact.objects.filter(name = "Shital Bharti")

'''