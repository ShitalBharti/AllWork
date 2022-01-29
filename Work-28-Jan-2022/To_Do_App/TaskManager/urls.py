from django.urls import path
from TaskManager import views


urlpatterns = [
    path('', views.show, name='show'),
    path('display', views.display, name='display'),
    path('create', views.create, name='create'),
    path('readall', views.readall, name='readall'),
    path('readid', views.readid, name='readid'),
]