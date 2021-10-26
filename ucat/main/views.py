from .models import Link
from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect,HttpResponse,HttpResponseNotFound
from django.views.decorators.http import require_http_methods
import random
import string

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def redirector(request, short): 
	link = get_object_or_404(Link, short = short)
	return render(request,'main/redirect.html',{'link':link})

def index(request):
	current_user = request.user 
	if current_user.id:
		username = current_user.username
		links = User.objects.get(id=current_user.id).link_set.order_by('-id')
		urls = []
		for link in links:
			urls.append(request.build_absolute_uri('c/'+link.short))
		ret = zip(links,urls)
		return render(request, 'main/index.html',{'links':links,'uid':current_user.id,'ret':ret,'username':username})
	else:
		return render(request, 'main/index.html',{'not_authorized':True})
def signin(request):
	if request.method == "POST":
		username = request.POST['username']
		pwd = request.POST['pwd']
		user = authenticate(username = username,password = pwd)
		if user is not None:
			login(request,user)
			return redirect('main:index')
		else:
			return render(request,'main/login.html',{'error':True})
	return render(request,'main/login.html')
def logout(request):
	auth_logout(request)
	return redirect('main:index')
def register(request):
	if request.method == "POST":
		print('123')
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request,user)
			messages.success(request,'Регистраия прошла успешно')
			return redirect('main:index')
		messages.error(request,'Неуспешная регистрация')
	form = NewUserForm()
	return render(request,'main/register.html',{'register_form':form})
def delete(request, short):
	if request.user.id:
		link = User.objects.get(pk = request.user.id).link_set.get(short=short) #находим ссылку и сразу проверяем делает ли запрос автор ссылки
		if link != None:
			link.delete()
			return redirect('main:index')
		else:
			return HttpResponse('Вы не являетесь автором данной ссылки и не можете его далить')
	return HttpResponse('Не авториирован!')
@require_http_methods(["POST"])
def add(request):
	if(request.user.id):
		link = request.POST['link']
		short = get_random_string(6)
		user = User.objects.get(pk=request.user.id)
		Link.objects.create(author=user,link=link,short=short)
		return HttpResponseRedirect('/')
	else:
		return HttpResponseNotFound('Not Allowed')