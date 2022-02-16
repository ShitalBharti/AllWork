from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuinfo/',views.student_detail),
    path('studinfo/<int:pk>',views.student_detail1),
    path('studlst/',views.student_list),
]
