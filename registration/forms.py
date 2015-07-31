from models import Registration
from django.forms import ModelForm, ValidationError
from django import forms
from django.contrib.auth.models import User
from django.contrib import auth

class RForm(ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model=Registration
		fields=['username', 'firstname', 'lastname', 'email', 'password', 'picture']

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