from django.shortcuts import render
from .forms import StudentRegisterationForm

# Create your views here.

def showformdata(request):
    fm = StudentRegisterationForm(auto_id='some_%s', label_suffix='-',initial={ 'name':'Sonam'} )
    # auto_id: id of html fields name
    fm.order_fields(field_order=['email','name','first_name'])
   # return render(request, 'useregister.html', {'form':fm})
   # return render(request, 'forregisteration.html', {'form': fm})
   # return render(request, 'hiddenregister.html', {'form': fm})
    return render(request, 'formfield.html', {'form': fm})

# auto_id = True, label_suffix = '-'





