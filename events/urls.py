
from django import urls
from django.conf.urls import url
from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.homepage,name="homepage"),
    path('deneme',views.deneme,name="deneme"),
    path('loginstudent/checkuser',views.checkuser,name="checkuser"),
    path('register/',views.register,name="register"),
    path('register/adduser',views.adduser,name="register"),
    #path('base',views.base,name="base"),
    path('checkuser',views.checkuser,name="checkuser"), 
    path('adduser',views.adduser,name="adduser"),
    path('login',views.loginstudent,name='loginstudent'),
    path('logingrad',views.logingrad,name='logingrad'),
    path('addgrad',views.addgrad,name='login'),
    path('checkgrad', views.checkgrad, name='checkgrad'),

    path('universitypage',views.universitypage,name="universitypage"),
    path('gotouniversity',views.gotouniversity,name="gotouniversity"),
    
    path('graduateloginpage',views.graduateloginpage,name="graduateloginpage"),
    path('ask_question' , views.ask_question , name="ask_question" ),

    path('graduateloginpage' , views.graduateloginpage , name="graduateloginpage" ),
    path('answer_question' , views.answer_question , name="answer_question" )

    

    
]
