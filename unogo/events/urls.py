
from django.urls import path,include
from . import views


urlpatterns = [
    #path('',views.hometester,name="home"),
    path('loginstudent/',views.home,name="userlogin"),
    path('loginstudent/checkuser',views.checkuser,name="checkuser"),
    path('register/',views.register,name="register"),
    path('register/adduser',views.adduser,name="register")

    
]
