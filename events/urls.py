
from django import urls
from django.conf.urls import url
from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.homepage,name="homepage"),
    path('loginstudent/',views.home,name="userlogin"),
    path('loginstudent/checkuser',views.checkuser,name="checkuser"),
    path('register/',views.register,name="register"),
    path('register/adduser',views.adduser,name="register"),
    #path('base',views.base,name="base"),
    path('checkuser',views.checkuser,name="checkuser"), 
    path('adduser',views.adduser,name="adduser"),
    path('login',views.loginstudent,name='login'),
    path('logingrad',views.logingrad,name='logingrad'),
    path('addgrad',views.addgrad,name='login'),

    path('universitypage',views.universitypage,name="universitypage"),
    path('gotouniversity',views.gotouniversity,name="gotouniversity"),

    

    
]
