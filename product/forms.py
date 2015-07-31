from django.forms import ModelForm, ValidationError
from models import *
import re
from django import forms
from django.contrib import auth
class UserForm(ModelForm):
	class Meta:
		model=User
		fields=['name','email']

class CategoryForm(ModelForm):
	choice=User.objects.all()
	user=forms.CheckboxSelectMultiple(choices=choice)
	class Meta:
		model=Category
		fields=['name','user']

	def clean_name(self):
		data=self.cleaned_data['name']
		if(data[0].isupper() and re.findall(r'[0-9]+',data)):
			return data
		else:
			raise ValidationError("Category name must startwith capital letter and must contains atleast a digit")

class ProductForm(ModelForm):
	class Meta:
		model=Product
		fields=['name','price','category']

class Login(forms.Form):
	username=forms.CharField(max_length=200)
	password=forms.CharField(widget=forms.PasswordInput)


class RegisterForm(ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)
	email=forms.EmailField()
	class Meta:
		model = auth.models.User
		fields = ['username','email','password']