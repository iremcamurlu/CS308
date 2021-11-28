from django.shortcuts import render
from .models import GradStudent, Usersv2
from .models import Student
from .models import Alluniv

# Create your views here.




def gotouniversity(request):
     unicode=request.GET.get('unicode')
     print(unicode)
     print(type(unicode))
     unicode=int(unicode)
     print(type(unicode))   

     all_univs=Alluniv.objects.all()

     for u1 in all_univs:
        print(type(u1.id))
        if(u1.id==unicode):
            univname=u1.univname
            univcity=u1.unicity
            print(univname)
            print(univcity)

            
            return render(request,'universitypage.html',{"univname":univname,"univcity":univcity})
     





def loginstudent(request):
    return render(request,'loginstudent.html')




def logingrad(request):
    return render(request,'logingraduate.html')


def homepage(request):
    return render(request,'homepage.html')


def universitypage(request):
    return render(request,'universitypage.html',{})



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
    all_students=Student.objects.all()

    all_grad=GradStudent.objects.all()
     
     #newuser=Users(username=uname,password=psw)
     #newuser.save()
    for s1 in all_students:
        if(s1.semail==email and s1.spass==psw):
            result="Login Succesfull"
            return render(request,'loginuserhomepage.html',{"uname":s1.sname})

    for g1 in all_grad:
        if(g1.gemail==email and g1.gpass==psw):
            result="Login Succesfull"
            return render(request,'loginuserhomepage.html',{"uname":g1.gname})

             
    

    return render(request,'unknown.html',{})


def checkgrad(request):

    email=request.GET.get('logemail')
    psw=request.GET.get('logpass')
    #uname=format(uname)
    print(email)
    print(psw)
    grad_student=GradStudent.objects.all()
     
     #newuser=Users(username=uname,password=psw)
     #newuser.save()
    for g1 in grad_student:
        if(g1.gemail==email and g1.gpass==psw):
            result="Login Succesfull"
            return render(request,'loginuserhomepage.html',{"uname":g1.gname})
        
             
    

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
    newuser=Student(sname=uname,spass=psw, semail=email)
    newuser.save()

    return render(request,'loginstudent.html',{})

def addgrad(request):
    uname=request.GET.get('logname')
    psw=request.GET.get('logpass')
    email=request.GET.get('logemail')
    univ=request.GET.get('loguniv')
    major=request.GET.get('logmajor')
    uname=format(uname)
    print(uname)
    print(psw)
    print(email)
    print(univ)
    print(major)
    newuser=GradStudent(gname=uname,gpass=psw, gemail=email,gmajor=major,guniv=univ )
    newuser.save()

    return render(request,'logingraduate.html',{})





