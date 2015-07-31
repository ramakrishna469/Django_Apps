from django.conf.urls import include, url
import views


urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),


    url(r'^users/$', views.users, name='users' ),
    url(r'^users/adduser/$', views.adduser, name='adduser'),
    url(r'^users/deluser/(?P<pk>[0-9]+)/$', views.deluser, name='deluser'),
    url(r'^users/edituser/(?P<pk>[0-9]+)/$', views.edituser, name='edituser'),
    url(r'^users/userviewcat/(?P<pk>[0-9]+)/$', views.userviewcat, name='userviewcat'),
    url(r'^users/userviewpro/(?P<pk>[0-9]+)/$', views.userviewpro, name='userviewpro'),


    url(r'^categories/$', views.categories, name='categories'),
    url(r'^categories/addcategory/$', views.addcategory, name='addcategory'),
    url(r'^categories/delcat/(?P<pk>[0-9]+)/$', views.delcat, name='delcat'),
    url(r'^categories/editcat/(?P<pk>[0-9]+)/$', views.editcat, name='editcat'),
    url(r'^categories/catviewpro/(?P<pk>[0-9]+)/$', views.catviewpro, name='catviewpro'),


    url(r'^products/$', views.products, name='products'),
    url(r'^products/addproduct/$', views.addproduct, name='addproduct'),
    url(r'^products/delpro/(?P<pk>[0-9]+)/$', views.delpro, name='delpro'),
    url(r'^products/editpro/(?P<pk>[0-9]+)/$', views.editpro, name='editpro'),
    url(r'^products/(?P<pk>[0-9]+)/$', views.basket, name='basket'),


    url(r'^logout/$', views.logout, name='logout'),
]