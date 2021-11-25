from django.shortcuts import render
from .models import Usersv2

# Create your views here.

def homepage(request):
    return render(request,'homepage.html')



def mainpage(request):
    return render(request,'mainpage.html')

def home(request):
    user=Usersv2.objects.all()
    contex={

        'user':user

    }

    
    return render(request,'home.html',{"user":user})



def checkuser(request):

    email=request.GET.get('logemail')
    psw=request.GET.get('logpass')
    #uname=format(uname)
    print(email)
    print(psw)
    user=Usersv2.objects.all()
     
     #newuser=Users(username=uname,password=psw)
     #newuser.save()
    for u1 in user:
        if(u1.email==email and u1.password==psw):
            result="Login Succesfull"
            return render(request,'mainpage.html',{"uname":u1.name})
        
             
    

    return render(request,'unknown.html',{})


def register(request):
    return render(request,'register.html',{})



def adduser(request):
    uname=request.GET.get('logname')
    psw=request.GET.get('logpass')
    email=request.GET.get('logemail')
    uname=format(uname)
    print(uname)
    print(psw)
    print(email)
    newuser=Usersv2(name=uname,password=psw, email=email)
    newuser.save()

    return render(request,'home.html',{})



def base(request):

    return render(request,'base.html',{})


