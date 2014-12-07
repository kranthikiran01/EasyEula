from django.shortcuts import render
from django.http import Http404,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from authentication.models import UserProfile
from authentication.forms import UserForm,UserProfileForm
from datetime import datetime
import os
# Create your views here.
def auth(request):
	current_page = "login"
	title = "Login"
	return render(request,'auth/login.html',{'current_page':current_page,'title':title})

def _login(request):
	if request.method=="POST":
		email = request.POST['email']
		password = request.POST['password']
		user = authenticate(username=email, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				user.last_login=datetime.now()
				user.ip_address=get_client_ip(request)
				user.save()
				if not request.POST.get('remember_me', None):
					request.session.set_expiry(0)
				messages.info(request,'Welcome '+user.username)
				return HttpResponseRedirect('/dashboard/')
			else:
				messages.info(request,'Your account is inactive. Contact webmaster')
				return HttpResponseRedirect('/auth')
		else:
			messages.error(request,'Invalid username/password')
			return HttpResponseRedirect('/auth')
	else:
		messages.info('bad request')
		return HttpResponseRedirect('/auth')

def _logout(request):
	logout(request)
	messages.info(request,'You have been logged out')
	return HttpResponseRedirect('/auth')

#Function get ip address of user
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def register(request):
	registered = False
	if request.method=="POST":
		user_form = UserForm(data = request.POST)
		profile_form = UserProfileForm(data = request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save(commit = False)
			user.set_password(user.password)
			user.last_login=datetime.now()
			user.is_active = True
			user.save()
			profile = profile_form.save(commit = False)
			print user
			profile.user = user
			profile.signUpDate=datetime.now()
			profile.ip_address = get_client_ip(request)
			print profile.ip_address
			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']
			profile.save()
			
			registered = True
		else:
			print 'user'+str(user_form.errors)
			print 'profile'+str(profile_form.errors)
			messages.info(request,str(user_form.errors)+str(profile_form.errors))
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
	return render(request,'auth/register.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})