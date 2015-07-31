from django import template
from product.models import Basket
import datetime
import time

register= template.Library()

@register.filter()
def check(user, product):
	if Basket.objects.filter(user=user, pname=product):
		return True
	else:
		return False

# register.filter('check', check)
@register.filter()
def timecheck(d1):
	a=time.time()
	now=datetime.datetime.now()
	d2=datetime.date(now.year, now.month, now.day)
	c=d1-d2
	days=c.days
	li=[0,0,0,0]
	print days
	if days<2:
		if days==1:
			return "Tomorrow"
		else:
			return "Today"
	else:
		while(days):
			if days>365:
				year=days/365
				days=days%365
				if year:
					li[0]=year
			elif(days > 30 and days<356):
				month=days/30
				days=days%30
				if month:
					li[1]=month
			elif days<30 and days>7:
				week=days/7
				days=days%7
				if week:
					li[2]=week
			elif days<7 and days>0:
				li[3]=days
				days=0
	st=""
	if len(li)!=0:
		for i in range(len(li)):
			if i==0 and li[i]!=0:
				st=st+str(li[i])+'years,'
			elif i==1 and li[i]!=0:
				st=st+str(li[i])+'months, '
			elif i==2 and li[i]!=0:
				st=st+str(li[i])+'weeks, '
			elif i==3 and li[i]!=0:
				st=st+str(li[i])+'days left'
		print time.time()-a
		return st






