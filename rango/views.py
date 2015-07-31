from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from forms import RegForm, UserForm, Login
from models import Reg
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User



def login(request):
	if request.user.is_active:
		return HttpResponseRedirect(reverse('rango:userdetails'))
	template_name='rango/login.html'
	form=Login()
	if request.method=='POST':
		form=Login(request.POST)
		if form.is_valid():
			username=request.POST['username']
			password=request.POST['password']
			print username,"hello "*10
			user=auth.authenticate(username=username, password=password)
			if user is not None and user.is_active:
				auth.login(request, user)
				return HttpResponseRedirect(reverse('rango:userdetails'))
		else:
			return render(request, template_name, {'form':form})
	else:
		return render(request, template_name, {'form':form})


def register(request):
	if request.user.is_active:
		return HttpResponseRedirect(reverse('rango:userdetails'))
	template_name='rango/register.html'
	user=UserForm()
	form=RegForm()
	if request.method=='POST':
		form = RegForm(request.POST, request.FILES)
		user = UserForm(request.POST)
		if user.is_valid() and form.is_valid():
			u=user.save()
			u.set_password(request.POST['password'])
			u.save()
			a=form.save(commit=False)
			a.picture=request.FILES['picture']
			a.user=u
			a.save()
			return HttpResponseRedirect(reverse('rango:login'))
		else:
			return render(request, template_name, {'form':[form,user]})
	else:
		return render(request, template_name, {'form':[form,user]})

def userdetails(request):
	if request.user.is_active:
		template_name='rango/userdetails.html'
		users=auth.models.User.objects.filter(username=request.user)
		profile=Reg.objects.filter(user=request.user)
		return render(request, template_name, {'users':users, 'profile':profile})
		return HttpResponse("hello")
	else:
		return HttpResponseRedirect(reverse('rango:login'))

def logout(request):
	if request.user.is_active:
		auth.logout(request)
		return HttpResponseRedirect(reverse('rango:login'))