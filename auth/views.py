from django.shortcuts import render
from django.http import Http404,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def auth(request):
	current_page = "login"
	title = "Login"
	return render(request,'auth/login.html',{'current_page':current_page,'title':title})

def _login(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			messages.info(request,'Welcome '+user.username)
			return HttpResponseRedirect('/dashboard')
		else:
			messages.info(request,'Your account is inactive. Contact webmaster')
			return HttpResponseRedirect('/auth')
	else:
		messages.error(request,'Invalid username/password')
		return HttpResponseRedirect('/auth')

def _logout(request):
	logout(request)
	messages.info(request,'You have been logged out')
	#print('Bye')
	return HttpResponseRedirect('/auth')