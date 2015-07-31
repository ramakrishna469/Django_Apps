from django.conf.urls import include, url
import views

urlpatterns = [

	url(r'^$', views.login, name='login'),
	url(r'^users/$', views.userdetails, name='userdetails'),
	url(r'^register/$', views.register, name='register'),
	url(r'^logout/$', views.logout, name='logout'),

]