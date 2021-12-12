from django.shortcuts import render
from .models import Users

# Create your views here.
def home(request):
    user=Users.objects.all()
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
    user=Users.objects.all()
     
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
    uname=format(uname)
    print(uname)
    print(psw)
    newuser=Users(name=uname,password=psw)
    newuser.save()

    return render(request,'register.html',{})

