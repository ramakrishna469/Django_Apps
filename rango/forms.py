from django.forms import ModelForm, ValidationError
from django import forms
from models import Reg
from django.contrib.auth.models import User
from django.contrib import auth


class UserForm(ModelForm):
	password=forms.CharField(widget = forms.PasswordInput)
	class Meta:
		model = User
		fields = ['username','first_name','last_name','email','password']

class RegForm(ModelForm):
	COURSE = [('Select', 'Select'),('BE/B.Tech', 'BE/B.Tech'),('M.Tech', 'M.Tech'),
			('B.Com', 'B.Com'),('B.Pharm', 'B.Pharm'),('B.A', 'B.A'),('M.Com', 'M.Com'),
	]
	course=forms.ChoiceField(choices=COURSE)

	BRANCH = [('Select', 'Select'),('ECE', 'ECE'),('Mechanical', 'Mechanical'),
			('Civil', 'Civil'),('EEE', 'EEE'),('Chemical', 'Chemical'),
			('Information Technology', 'Information Technology'),
	]
	branch=forms.ChoiceField(choices=BRANCH)



	class Meta:
		model=Reg
		fields=['course','branch','percentage','picture','mobile']

class Login(forms.Form):
	username=forms.CharField(max_length=200)
	# email=forms.EmailField(max_length=200)
	password=forms.CharField(widget=forms.PasswordInput)

	def clean(self):
		users=User.objects.all()
		username=self.cleaned_data.get('username')
		password=self.cleaned_data.get('password')
		user=auth.authenticate(username=username, password=password)
		if not user or not user.is_active:
			raise ValidationError("You Entered Wrong Username or Password please try again")
		else:
			return self.cleaned_data