from django.db import models
from django.contrib.auth.models import User

class Reg(models.Model):
	user = models.OneToOneField(User)
	course = models.CharField(max_length=200)
	branch = models.CharField(max_length=200)
	percentage = models.FloatField()
	picture = models.ImageField(upload_to='profile_pics/')
	mobile = models.IntegerField()

	def __unicode__(self):
		return self.user.username


