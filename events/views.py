from django.http import request
from django.shortcuts import render
from datetime import date
from .models import GradStudent, Usersv2
from .models import Student
from .models import Alluniv
from .models import Question
from .models import Unimajors


# Create your views here.

def take_comments(unicode,order):
   

 

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
 


        current.append(q1.day)
        current.append(q1.like)
        questionss.append(current)

    print(questionss)

    for u1 in all_univs:
        #print(u1.univname)
        if(u1.id==unicode):
            univname=u1.univname
            univcity=u1.unicity
            uninfo=u1.uninfo
            uniface=u1.uniface
            uninsta=u1.uninsta
            unitwitter=u1.unitwitter
            unisite=u1.unisite
            

    
  
    



    return ques , ans , student_of_questions, univname, univcity, questionss,uninfo,uniface,uninsta,unitwitter,unisite


def take_comment_studentid(id):

   
    #print('take comment unicode type',type(unicode))
    
    questions = Question.objects.all()



    ques = "str"
    ans = "ans"
    student_of_questions = "a"
    univname="ss"
    univcity="aa"
    questionss=[] #questions[0][...] for questions #questions[1][...] for answers #questions[2][...] for sid
            
    for q1 in questions:
       print("TYPE OF UNİCODE İS ",type(id))
       print("TYPE OF univid İS ",type(q1.sid))
       print("TYPE OF id İS ",id)
       print("TYPE OF q1.sid İS ",q1.sid)

       
       
       if id==int(q1.sid):
        
        current = []
        current.append(q1.question)
        current.append(q1.answer)
        current.append(q1.id)

        

        questionss.append(current)

    print(questionss)


    return questionss




def takeunimajors(unicode):
   
   
    #print('take comment unicode type',type(unicode))
    

    all_majors=Unimajors.objects.all()


    majors=[] #questions[0][...] for questions #questions[1][...] for answers #questions[2][...] for sid
            

    print("type of unicode is ",type(unicode))

    print(" unicode is ",unicode)

    

    
    for m1 in all_majors:
        if m1.univid==str(unicode):
            current = []
            current.append(m1.id)
            current.append(m1.majorname)
            current.append(m1.max)
            current.append(m1.min)
            majors.append(current)



    #majors [0][...] for id #questions[1][...] for majorname #questions[2][...] for max #questions[3][...] for min
    return majors







def gotouniversity(request):

     unicode=request.GET.get('unicode')
     page_sid = request.GET.get('sid')
     customer = request.GET.get('customer')

     unicode=int(unicode)

     print("UNICODE IS ",unicode)
     print("CUSTOMER IS ",customer)
     print("CUSTOMER TYPE IS ",type(customer))
     ques, ans , questionner_id, univname, univcity, questions,uninfo,uniface,uninsta,unitwitter,unisite = take_comments(unicode,0)

     majors=takeunimajors(unicode)


            
     return render(request,'universitypage.html',{"questionss":questions ,"page_sid":page_sid ,"unicode":unicode,"univname":univname,"univcity":univcity,"question":ques, "answer":ans, "stu_name":questionner_id,"customer":customer,"majors":majors ,"uninfo":uninfo,"uniface":uniface,"uninsta":uninsta,"unitwitter":unitwitter,"unisite":unisite})
    



def admin_get_question():

    questions = Question.objects.all()
    ques = "str"
    ques_id="a"
    allquestions=[] 
    print("Outside for")
    for q1 in questions:
       
     current = []
     current.append(q1.id)
     current.append(q1.question)
     current.append(q1.answer)

     #id question answer
     
     allquestions.append(current)    


    return allquestions


def ask_question(request):


    comment=request.GET.get('comment')
    unicode=request.GET.get('unicode')
    page_sid = request.GET.get("page_sid")
    customer = request.GET.get('customer')


    s1 = Student.objects.get(id=page_sid)

    #print(s1.sname)


    today = date.today()
    print("Today's date:", today)
    
    day = today.strftime("%D")
    print("today:", day)
    print("type of date is ",type(day))


    
    
    print('comment ' , comment)
    print("Unicode ",unicode," sid ",page_sid," Comment ",comment)

    new_comment =Question(univid = str(unicode) , sid = page_sid, question = comment,day=day,like=0)
    new_comment.save()
    unicode = int(unicode)

    ques, ans , questionner_id, univname, univcity, questions,uninfo,uniface,uninsta,unitwitter,unisite = take_comments(unicode,0)

    majors=takeunimajors(unicode)



    return render(request,'universitypage.html',{"questionss":questions,"page_sid":page_sid ,"unicode":unicode,"univname":univname,"univcity":univcity,"question":ques, "answer":ans, "stu_name":questionner_id,"customer":customer,"majors":majors,"uninfo":uninfo,"uniface":uniface,"uninsta":uninsta,"unitwitter":unitwitter,"unisite":unisite})
    
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


    ques, ans , questionner_id, univname, univcity, questions,uninfo,uniface,uninsta,unitwitter,unisite = take_comments(int(unicode),0)


    return render(request, 'graduateloginpage.html', {"questionss":questions,"page_sid":page_sid ,"unicode":unicode,"univname":univname,"univcity":univcity,"question":ques, "answer":ans, "stu_name":questionner_id,"uninfo":uninfo,"uniface":uniface,"uninsta":uninsta,"unitwitter":unitwitter,"unisite":unisite})



def graduateloginpage(request):



    return render(request,'graduateloginpage.html',{})



def adminpage(request):
    return render(request,'adminpage.html',{})





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


    
    return render(request,'deneme.html',{})



def delete_question(request):
    
    qid=request.GET.get('questionid')
    questions=admin_get_question()
    print("ID of the question is ",qid )
    print("type of the question is ",type(qid) )
    instance = Question.objects.get(id=int(qid))
    instance.delete()
    questions=admin_get_question()

    return render(request,'adminpage.html',{"questions":questions})

    
def add_university(request):
    questions=admin_get_question()
    uniname=request.GET.get('uniname')
    unicity=request.GET.get('unicity')

    print("NAME İS ",uniname)
    print("CİTY İS ",unicity)

    newuniv=Alluniv(univname=uniname,unicity=unicity)
    newuniv.save()

    return render(request,'adminpage.html',{"questions":questions})




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
            if(s1.sstatus=="1"):
                questions=admin_get_question()
                return render(request,'adminpage.html',{"questions":questions})
            else:
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

    ques, ans , questionner_id, univname, univcity, questions,uninfo,uniface,uninsta,unitwitter,unisite = take_comments(unicode,0)

                     
    return render(request,'graduateloginpage.html',{ "grad_id": grad_id,"uname":g1.gname, "questionss":questions,"unicode":unicode,"univname":univname,"univcity":univcity,"question":ques, "answer":ans, "stu_name":questionner_id})



def register(request):
    return render(request,'register.html',{})


def userpage(request,id):

    
    stu = Student.objects.get(id=id)
    name=stu.sname
    email=stu.semail
    questions=take_comment_studentid(id)

    return render(request,'userpage.html',{"name":name,"email":email,"questions":questions})



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




def likecomment(request):
   
    qid=request.GET.get('qid')
    unicode=request.GET.get('unicode')
    page_sid = request.GET.get("page_sid")
    customer = request.GET.get('customer')
    print("ALLAH İÇİN ÇALIŞ ARTIK",unicode)
    
    majors=takeunimajors(unicode)

    print("QİD OF This comment is ",qid)
    print("TYPE OF This comment is ",type(qid))

 


    instance = Question.objects.get(id=int(qid))
    
    instance.like=instance.like+1
    instance.save()
    ques, ans , questionner_id, univname, univcity, questions,uninfo,uniface,uninsta,unitwitter,unisite = take_comments(int(unicode),0)

    return render(request,'universitypage.html',{"questionss":questions,"page_sid":page_sid ,"unicode":unicode,"univname":univname,"univcity":univcity,"question":ques, "answer":ans, "stu_name":questionner_id,"customer":customer,"majors":majors,"uninfo":uninfo,"uniface":uniface,"uninsta":uninsta,"unitwitter":unitwitter,"unisite":unisite})
    



def rankingenter(request):
   
    return render(request,'rankingenter.html')



def rankingenterresult(request):
    ranking=request.GET.get('ranking')
    all_majors=Unimajors.objects.all()
    majors=[]
    print("Ranking is ",ranking)
    print("Type is ",type(ranking))



    for m1 in all_majors:
        
        if int(ranking)<int(m1.min) :

            u1 = Alluniv.objects.get(id=m1.univid)
             # change field
       
            current = []

            current.append(m1.id)
            current.append(u1.univname)
            current.append(m1.majorname)
            current.append(m1.max)
            current.append(m1.min)
            majors.append(current)


    print(majors)
    


    return render(request,'rankingenterresult.html',{"majors":majors})




def sortby(request):
    #unicode=request.GET.get('unicode')
     dropdown = request.GET['orders'] 
     print("DROPDOWN İS",dropdown)

     unicode=request.GET.get('unicode')
     page_sid = request.GET.get('page_sid')
     customer = request.GET.get('customer')

     #unicode=int(unicode)u

     print("UNICODE IS ",unicode)
     print("CUSTOMER IS ",customer)
     print("CUSTOMER TYPE IS ",type(customer))
     if dropdown=="likeas":
         ques, ans , questionner_id, univname, univcity, questions,uninfo,uniface,uninsta,unitwitter,unisite = take_comments(int(unicode),1)
     elif dropdown=="likedes":
        ques, ans , questionner_id, univname, univcity, questions,uninfo,uniface,uninsta,unitwitter,unisite = take_comments(int(unicode),2)
     elif dropdown=="dayas":
        ques, ans , questionner_id, univname, univcity, questions,uninfo,uniface,uninsta,unitwitter,unisite = take_comments(int(unicode),3)
     elif dropdown=="daydes":
        ques, ans , questionner_id, univname, univcity, questions,uninfo,uniface,uninsta,unitwitter,unisite = take_comments(int(unicode),4)
     
     
     majors=takeunimajors(unicode)



     return render(request,'universitypage.html',{"questionss":questions ,"page_sid":page_sid ,"unicode":unicode,"univname":univname,"univcity":univcity,"question":ques, "answer":ans, "stu_name":questionner_id,"customer":customer,"majors":majors ,"uninfo":uninfo,"uniface":uniface,"uninsta":uninsta,"unitwitter":unitwitter,"unisite":unisite})
    




    
