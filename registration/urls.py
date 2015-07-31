from django.conf.urls import include, url
import views
from django.conf import settings


urlpatterns = [

	url(r'^$', views.login, name='login'),
	url(r'^accounts/login/$', views.login, name='login'),
	url(r'^register/$', views.register, name='register'),
	url(r'user_details/$', views.userdetails, name='userdetails'),
	url(r'user_details/logout/$', views.user_logout, name='user_logout'),
	url(r'^media/registration/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),

]


