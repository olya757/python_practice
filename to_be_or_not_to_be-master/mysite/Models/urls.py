from django.urls import path

from . import views
from django.conf.urls import url
from .models import *
from django.urls import path, include

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.Home.as_view(template_name='home.html'), name='index'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('home/', views.Home.as_view(template_name='home.html'), name='home'),
    path('table', views.select_in_home, name='select_in_home'),
    #path('visiting/', views.Visiting.as_view(template_name='visiting.html'),name='visiting'),
    #path('visiting/save/', views.Visiting.save, name='save'),
    path('<int:gc_id>/<str:date>/save',views.save, name='save')

]