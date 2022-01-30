from django.urls import path
from TaskManager import views


urlpatterns = [
    path('', views.show, name='show'),
    path('display', views.display, name='display'),
    path('create', views.create, name='create'),
    path('read', views.read, name='read'),
    path('readid', views.readid, name='readid'),
    path('delete', views.delete, name='delete'),
    path('update', views.update, name='update'),
]