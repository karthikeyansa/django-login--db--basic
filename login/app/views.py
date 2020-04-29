from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import User
from .forms import Sign,Index

def welcome(request,id):
	user = get_object_or_404(User,pk = id)
	return render(request,'login/welcome.html',{'name':user.name,'password':user.password})

def sign(request):
	if request.method == 'POST':
		form = Sign(request.POST)
		if form.is_valid():
			new = User.objects.get(name = request.POST['name'])
			if not new:
				new = User(name = request.POST['name'],password=request.POST['password'])
				new.save()
				return redirect(welcome,id = new.id)
			else:
				return render(request,'login/sign.html',{'msg':'user already exists'})
	else:
		form = Sign()
	context = {'form':form}
	return render(request,'login/sign.html',context)

def index(request):
	if request.method == 'POST':
		form = Index(request.POST)
		if form.is_valid():
			name = request.POST['name']
			password = request.POST['password']
			user = get_object_or_404(User,name = name,password = password)
			if user:
				return redirect(welcome,id = user.id)
				
	else:
		form = Index()
	context = {'form':form}
	return render(request,'login/index.html',context,)