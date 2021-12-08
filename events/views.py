from django.shortcuts import render
from .models import GradStudent, Usersv2
from .models import Student
from .models import Alluniv
from .models import Question


# Create your views here.

def take_comments(unicode):
   
    #print('take comment unicode type',type(unicode))
    

    all_univs=Alluniv.objects.all()
    questions = Question.objects.all()
    all_students = Student.objects.all()

    ques = "str"
    ans = "ans"
    student_of_questions = "a"
    univname="ss"
    univcity="aa"
    questionss=[] #questions[0][...] for questions #questions[1][...] for answers #questions[2][...] for sid
            
    for q1 in questions:
       print("TYPE OF UNİCODE İS ",type(unicode))
       print("TYPE OF univid İS ",type(q1.univid))
       univid=int(q1.univid)
       if univid==unicode:

        current = []
        current.append(q1.question)
       
        current.append(q1.answer)
        stu_id = q1.sid
        current.append(q1.id)
        for sti in all_students:
             if stu_id == str(sti.id):
                current.append(sti.sname)
        print(current)

        questionss.append(current)

    #print(questions)

    for u1 in all_univs:
        #print(u1.univname)
        if(u1.id==unicode):
            univname=u1.univname
            univcity=u1.unicity


    return ques , ans , student_of_questions, univname, univcity, questionss


def gotouniversity(request):

     unicode=request.GET.get('unicode')
     page_sid = request.GET.get('sid')
     customer = request.GET.get('customer')

     unicode=int(unicode)

     print("UNICODE IS ",unicode)
     print("CUSTOMER IS ",customer)
     print("CUSTOMER TYPE IS ",type(customer))


     ques, ans , questionner_id, univname, univcity, questions = take_comments(unicode)

            
     return render(request,'universitypage.html',{"questionss":questions ,"page_sid":page_sid ,"unicode":unicode,"univname":univname,"univcity":univcity,"question":ques, "answer":ans, "stu_name":questionner_id,"customer":customer})
     
    

def ask_question(request):


    comment=request.GET.get('comment')
    unicode=request.GET.get('unicode')
    page_sid = request.GET.get("page_sid")
    customer = request.GET.get('customer')


    s1 = Student.objects.get(id=page_sid)

    #print(s1.sname)


    
    
    print('comment ' , comment)
    print("Unicode ",unicode," sid ",page_sid," Comment ",comment)

    new_comment =Question(univid = str(unicode) , sid = page_sid, question = comment)
    new_comment.save()
    unicode = int(unicode)

    ques, ans , questionner_id, univname, univcity, questions = take_comments(unicode)


    return render(request,'universitypage.html',{"questionss":questions,"page_sid":page_sid ,"unicode":unicode,"univname":univname,"univcity":univcity,"question":ques, "answer":ans, "stu_name":questionner_id,"customer":customer})
    
def answer_question(request):


    unicode=request.GET.get('unicode')
    page_sid = request.GET.get('Grad_id')
    ques_id =request.GET.get('ques_id')
    Answer = request.GET.get('Answer') 

    print("answerr   cevabi" , Answer)
    print("question id ", ques_id)
    q = Question.objects.get(id=ques_id)
    q.answer = Answer  # change field
    q.gid = page_sid
    q.save() # this will update only


    ques, ans , questionner_id, univname, univcity, questions = take_comments(int(unicode))


    return render(request, 'graduateloginpage.html', {"questionss":questions,"page_sid":page_sid ,"unicode":unicode,"univname":univname,"univcity":univcity,"question":ques, "answer":ans, "stu_name":questionner_id})



def graduateloginpage(request):




    return render(request,'graduateloginpage.html',{})







def loginstudent(request):
    return render(request,'loginstudent.html')




def logingrad(request):

    return render(request,'logingraduate.html')


def homepage(request):
    univs=getUniv()
    return render(request,'homepage.html',{"univs":univs})


def universitypage(request):

    return render(request,'universitypage.html',{})



def mainpage(request):
    return render(request,'mainpage.html')

def deneme(request):
    user=Usersv2.objects.all()
    contex={

        'user':user

    }

    
    return render(request,'deneme.html',{"user":user})





def getUniv():
    all_univs=Alluniv.objects.all()
    univs=[]
    for u1 in all_univs:
       current = []
       current.append(u1.id)
       
       current.append(u1.univname)
       current.append(u1.unicity)
      

       univs.append(current)

    return univs









def checkuser(request):

    email=request.GET.get('logemail')
    psw=request.GET.get('logpass')
    #uname=format(uname)
    print(email)
    print(psw)
    all_students=Student.objects.all()
    univs=getUniv()

    for s1 in all_students:
        if(s1.semail==email and s1.spass==psw):
            result="Login Succesfull"
            return render(request,'loginuserhomepage.html',{"uname":s1.sname , "sid":s1.id,"univs":univs})
             
    

    return render(request,'unknown.html',{})


def checkgrad(request):

    email=request.GET.get('logemail')
    psw=request.GET.get('logpass')

    grad_student= GradStudent.objects.all()

    print(email)
    print(psw)
    true_user = False
    unicode =''
    for g1 in grad_student:
        if(g1.gemail==email and g1.gpass==psw):
            result="Login Succesfull"
            true_user = True
            
        
    if(true_user == False):
        return render(request,'unknown.html',{})

    grad_id = 0

    for each in grad_student:
        if(each.gemail == email):
            print(each.gemail)
            grad_id = each.id
            unicode = each.guniv

            break

    unicode = int(unicode)

    ques, ans , questionner_id, univname, univcity, questions = take_comments(unicode)

                     
    return render(request,'graduateloginpage.html',{ "grad_id": grad_id,"uname":g1.gname, "questionss":questions,"unicode":unicode,"univname":univname,"univcity":univcity,"question":ques, "answer":ans, "stu_name":questionner_id})



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





