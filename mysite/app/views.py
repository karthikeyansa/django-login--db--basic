from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse

def login(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        checkuser = authenticate(username = name,password = password)
        if checkuser:
            return HttpResponse(name,status=200)
        else:
            return HttpResponse('user not found',status=200)
    else:
        return render(request,'mysite/login.html')

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        try:
            newuser = User.objects.create_user(username = name,email=None,password=password)
            return redirect(login)
        except:
            return HttpResponse('no user created')
    else:
        return render(request,'mysite/register.html')

