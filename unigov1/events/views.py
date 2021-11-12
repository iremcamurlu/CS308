from django.shortcuts import render
from .models import Usersv2

# Create your views here.
def home(request):
    user=Usersv2.objects.all()
    contex={

        'user':user

    }

    
    return render(request,'home.html',{"user":user})



def checkuser(request):

    uname=request.GET.get('uname')
    psw=request.GET.get('psw')
    uname=format(uname)
    print(uname)
    print(psw)
    user=Usersv2.objects.all()
     
     #newuser=Users(username=uname,password=psw)
     #newuser.save()
    for u1 in user:
        if(u1.name==uname and u1.password==psw):
            result="Login Succesfull"
            return render(request,'known.html',{"uname":uname})
        
             
    

    return render(request,'unknown.html',{})


def register(request):
    return render(request,'register.html',{})



def adduser(request):
    uname=request.GET.get('uname')
    psw=request.GET.get('psw')
    email=request.GET.get('Email')
    uname=format(uname)
    print(uname)
    print(psw)
    print(email)
    newuser=Usersv2(name=uname,password=psw, email=email)
    newuser.save()

    return render(request,'home.html',{})

