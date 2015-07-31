from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from forms import RForm, Login
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from models import Registration


def login(request):
	# if(not request.user.is_authenticated)
	template_name='registration/login.html'
	form=Login()
	if(request.method=='POST'):
		form=Login(request.POST)
		if form.is_valid():
			username=request.POST['username']
			password=request.POST['password']
			user=auth.authenticate(username=username, password=password)
			if user is not None and user.is_active:
				auth.login(request, user)
				return HttpResponseRedirect('user_details/')
			else:
				return HttpResponseRedirect('register/')

	return render(request, template_name, {'form':form})


def register(request):
	template_name='registration/register.html'
	form=RForm()
	if(request.method=='POST'):
		form=RForm(request.POST)
		if form.is_valid():
			if('picture' in request.FILES):
				# form.picture=request.FILES['picture']
				a=form.save()
				a.picture=request.FILES['picture']
				a.save()
			username=request.POST['username']
			firstname=request.POST['firstname']
			lastname=request.POST['lastname']
			email=request.POST['email']
			password=request.POST['password']
			user=User.objects.create(username=username, first_name=firstname, last_name=lastname, email=email)
			user.set_password(password)
			user.save()
			return HttpResponse("Success")
	return render(request, template_name, {'form':form})


@login_required(login_url='/registration/')
def userdetails(request):
	template_name='registration/user_details.html'
	users=Registration.objects.all()
	dict_items={}
	for user in users:
		if user.email == request.user.email:
			dict_items={'user':user}
	return render(request, template_name, dict_items)

def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('registration:login'))
