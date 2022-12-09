
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def index(request):
    return render(request,'index.html')

def logins(request):
    if(request.method=='POST'):
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('/')
        else:
            msg=('Incorrect Password')
            return render(request,'login.html',locals())
    return render(request,'login.html')


def regist(request):
    if(request.method=='POST'):
        username=request.POST.get('username')
        password=request.POST.get('password')
        password2=request.POST.get('password2')
        email=request.POST.get('email')
        if(password!=password2):
            msg='the confirmed password not matched'
            return render(request,'regist.html',locals())
        elif username=='':
            msg='password should not be null'
            return render(request,'regist.html',locals())
        cuser=User.objects.create_user(username=username,password=password,email=email)
        cuser.save()
        return redirect('/login/')
    return render(request,'regist.html')


def log_out(request):
    logout(request)
    return redirect('/')




