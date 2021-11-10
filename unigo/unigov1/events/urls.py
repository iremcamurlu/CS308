
from django.urls import path,include
from . import views


urlpatterns = [
    #path('',views.hometester,name="home"),
    path('loginstudent/',views.home,name="userlogin"),
    path('loginstudent/checkuser',views.checkuser,name="checkuser"),

    
]
