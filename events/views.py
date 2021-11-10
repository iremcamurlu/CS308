from django.shortcuts import render
from .models import Users

# Create your views here.
def home(request):
    user=Users.objects.all()
    contex={

        'user':user

    }

    
    return render(request,'home.html',{"user":user})