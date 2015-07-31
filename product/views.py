from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import *
from forms import *
from django.contrib import auth
from django.contrib.auth.decorators import login_required
import datetime
import time


def login(request):
	template_name='product/login.html'
	if request.user.is_active:
		return render(request,'product/index.html')
	else:
		form=Login()
		if(request.method=='POST'):
			form=Login(request.POST)
			if form.is_valid():
				username=request.POST.get('username')
				password=request.POST.get('password')
				user=auth.authenticate(username=username, password=password)
				if user is not None and user.is_active:
					auth.login(request, user)
					request.session['user_id']=user.id
					return render(request,'product/index.html')
		return render(request,template_name,{'form':form})


def register(request):
	template_name='register.html'
	form=RegisterForm()
	if request.method=='POST':
		form=RegisterForm(request.POST)
		if form.is_valid():
			a=form.save()
			a.set_password(request.POST['password'])
			a.save()
			return HttpResponseRedirect(reverse('product:login'))
		else:
			return render(request, template_name, {'form':form})
	else:
		return render(request, template_name, {'form':form})

@login_required
def index(request):
	template_name='product/index.html'
	return render_to_response(template_name)


def users(request):
	template_name='product/users.html'
	if request.user.is_active:
		userobj=User.objects.all()
		catobj=Category.objects.all()
		li=[]
		licount=[]
		for user in userobj:
			li.append(user.category_set.all())
		for l1 in li:
			count=0
			for l2 in l1:
				count=count+l2.product_set.all().count()
			licount.append(count)
		z=zip(userobj,licount)
		dict_items={'z':z}
		return render(request,template_name,dict_items)
	else:
		return HttpResponseRedirect(reverse('product:login'))


def adduser(request):
	template_name='product/adduser.html'
	if request.user.is_active:
		form=UserForm()
		if(request.method=='POST'):
			form=UserForm(request.POST)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect(reverse('product:users'))
		return render(request,template_name,{'form':form})
	else:
		return HttpResponseRedirect(reverse('product:login'))


def deluser(request, pk):
	if request.user.is_active:
		user=User.objects.get(id=pk)
		user.delete()
		return HttpResponseRedirect(reverse('product:users'))
	else:
		return HttpResponseRedirect(reverse('product:login'))


def userviewcat(request, pk):
	template_name='product/userviewcat.html'
	if request.user.is_active:
		user=User.objects.get(id=pk)
		catobj=Category.objects.filter(user=user)
		dict_items={'catobj':catobj,'user':user}
		return render(request,template_name,dict_items)
	else:
		return HttpResponseRedirect(reverse('product:login'))


def userviewpro(request, pk):
	template_name='product/userviewpro.html'
	if request.user.is_active:
		user=User.objects.get(id=pk)
		catobj=Category.objects.filter(user=user)
		li=[]
		for p1 in catobj:
			li.append(p1.product_set.all())
		dict_items={'li':li,'user':user}
		return render(request,template_name,dict_items)
	else:
		return HttpResponseRedirect(reverse('product:login'))


def edituser(request, pk):
	template_name='product/edituser.html'
	if request.user.is_active:
		user=User.objects.get(id=pk)
		form=UserForm(instance=user)
		if(request.method=='POST'):
			form=UserForm(request.POST,instance=user)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect(reverse('product:users'))
		return render(request,template_name,{'form':form, 'user':user})
	else:
		return HttpResponseRedirect(reverse('product:login'))


def categories(request):
	if request.user.is_active:
		template_name='product/categories.html'
		catobj=Category.objects.all()
		dict_items={'catobj':catobj}
		return render(request,template_name,dict_items)
	else:
		return HttpResponseRedirect(reverse('product:login'))


def addcategory(request):
	if(request.session['user_id']):
		template_name='product/addcategory.html'
		form=CategoryForm()
		if(request.method=='POST'):
			form=CategoryForm(request.POST)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect(reverse('product:categories'))
		return render(request,template_name,{'form':form})
	else:
		return HttpResponseRedirect(reverse('product:login'))


def delcat(request, pk):
	if request.user.is_active:
		cat=Category.objects.get(id=pk)
		cat.delete()
		return HttpResponseRedirect(reverse('product:categories'))
	else:
		return HttpResponseRedirect(reverse('product:login'))


def editcat(request, pk):
	if(request.session['user_id']):
		template_name='product/editcat.html'
		cat=Category.objects.get(id=pk)
		form=CategoryForm(instance=cat)
		if(request.method=='POST'):
			form=CategoryForm(request.POST,instance=cat)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect(reverse('product:categories'))
		return render(request,template_name,{'form':form, 'cat':cat})
	else:
		return HttpResponseRedirect(reverse('product:login'))


def catviewpro(request, pk):
	if request.user.is_active:
		template_name='product/catviewpro.html'
		cat=Category.objects.get(id=pk)
		li=[]
		for pro in cat.product_set.all():
			li.append(pro)
		dict_items={'li':li,'cat':cat}
		return render(request,template_name,dict_items)
	else:
		return HttpResponseRedirect(reverse('product:login'))


def products(request):
	if request.user.is_active:
		template_name='product/products.html'
		probj=Product.objects.all()
		basket_obj=Basket.objects.filter(user=request.user)
		d1=datetime.date(2016, 11, 13)
		dict_items={'probj':probj, 'basket_obj':basket_obj, 'd1':d1}
		return render(request,template_name,dict_items)
	else:
		return HttpResponseRedirect(reverse('product:login'))


def addproduct(request):
	if request.user.is_active:
		template_name='product/addproduct.html'
		form=ProductForm()
		if(request.method=='POST'):
			form=ProductForm(request.POST)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect(reverse('product:products'))
		return render(request,template_name,{'form':form})
	else:
		return HttpResponseRedirect(reverse('product:login'))


def delpro(request, pk):
	if request.user.is_active:
		pro=Product.objects.get(id=pk)
		pro.delete()
		return HttpResponseRedirect(reverse('product:products'))
	else:
		return HttpResponseRedirect(reverse('product:login'))


def editpro(request, pk):
	if(request.session['user_id']):
		template_name='product/editpro.html'
		pro=Product.objects.get(id=pk)
		form=ProductForm(instance=pro)
		if(request.method=='POST'):
			form=ProductForm(request.POST,instance=pro)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect(reverse('product:products'))
		return render(request,template_name,{'form':form, 'pro':pro})
	else:
		return HttpResponseRedirect(reverse('product:login'))


def basket(request, pk):
	template_name='product/products.html'
	if request.method=='GET':
		basket_obj=Basket.objects.create(user=request.user, pname=Product.objects.get(id=pk))
		return HttpResponseRedirect(reverse('product:products'))

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect(reverse('product:login'))