from django.urls import path
from TaskManager import views


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('tasks/', views.show, name='show'),
    path('tasks/create', views.create, name='create'),
    path('tasks/read', views.read, name='read'),
    path('tasks/read/readid', views.readid, name='readid'),
    path('tasks/delete', views.delete, name='delete'),
    path('tasks/update', views.update, name='update'),
]