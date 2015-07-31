from django.db import models
from django import forms

class Registration(models.Model):
	username=models.CharField(max_length=200)
	firstname=models.CharField(max_length=200)
	lastname=models.CharField(max_length=200)
	email=models.EmailField(max_length=100, unique=True)
	password=models.CharField(max_length=20)
	picture=models.ImageField(upload_to='profile_images/', blank=True)

	def __str__(self):
		return self.username
