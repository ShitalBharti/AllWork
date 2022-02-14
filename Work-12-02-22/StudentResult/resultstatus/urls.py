from django.urls import path
from resultstatus import views


urlpatterns = [
    path('', views.home, name='home'),

    path('insert/', views.insertMarks, name='insertMarks'),
    path('displayAll/', views.displayMarks, name='displayMarks'),
    path('displayone/', views.displayMarksID, name='displayMarksID'),
    path('updateone/', views.updateMarks, name='updateMarks'),
    path('deleteone/', views.deleteRecord, name='deleteRecord'),
]