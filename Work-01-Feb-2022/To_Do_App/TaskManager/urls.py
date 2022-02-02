from django.urls import path
from TaskManager import views


urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('actions', views.show, name='show'),
    path('display', views.display, name='display'),
    path('create', views.create, name='create'),
    path('read', views.read, name='read'),
    path('readid', views.readid, name='readid'),
    path('delete', views.delete, name='delete'),
    path('update', views.update, name='update'),
]