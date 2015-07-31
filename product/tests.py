from django.test import TestCase
from .models import User, Category, Product
from .forms import UserForm, CategoryForm, ProductForm, Login
from django.test import Client


class ModelsUserTest(TestCase):
	def test_object_creation(self):
		self.assertEquals(User.objects.count(), 0)
		user=User.objects.create(name='Ram', email='ram@gmail.com')
		self.assertTrue(User.objects.count())
		self.assertEquals(User.objects.count(), 1)
		print ">>>>User object creation<<<<"

	def test_object_deletion(self):
		self.assertEquals(User.objects.count(),0)
		user=User.objects.create(name='Ram', email='ram@gmail.com')
		self.assertEquals(User.objects.count(), 1)
		user.delete()
		self.assertFalse(User.objects.count())
		self.assertEquals(User.objects.count(), 0)
		print ">>>>User object deletion<<<<"


class ModelsCategoryTest(TestCase):
	def setUp(self):
		self.user=User.objects.create(name='Ram', email='ram@gmail.com')

	def test_object_creation(self):
		self.assertEquals(Category.objects.count(), 0)
		cat=Category.objects.create(name='Mobile1')
		cat.user.add(self.user)
		cat.save()
		self.assertEquals(Category.objects.count(), 1)
		print ">>>>Category object creation<<<<"


class FormsTest(TestCase):
	def setUp(self):
		self.user_fields={'name':'Rama Krishna', 'email':'ramakrishna469@gmail.com'}

		self.user=User.objects.create(name='Sairam', email='sairam@gmail.com')
		self.cat_fields={'name':'Mobile3', 'user':[self.user.id]}

		self.cat=Category.objects.create(name='Mobile4')
		self.pro_fields={'name':'Samsung', 'price':5000, 'category':self.cat.id}

	def test_userform_testing(self):
		user=UserForm(self.user_fields)
		self.assertTrue(user.is_valid())
		self.assertEquals(user.is_valid(), True)
		print ">>>>UserForm Validation Check<<<<"

	def test_categoryform_testing(self):
		cat=CategoryForm(self.cat_fields)
		self.assertTrue(cat.is_valid())
		self.assertEquals(cat.is_valid(), True)
		print ">>>>CategoryForm Validation Check<<<<"

	def test_productform_testing(self):
		pro=ProductForm(self.pro_fields)
		self.assertTrue(pro.is_valid())
		print ">>>>ProductForm Validation Check<<<<"


class UrlsTest(TestCase):
	def setUp(self):
		self.client=Client()

	def test_urls(self):
		response=self.client.get('/product/')
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'product/login.html')

		response1=self.client.get('/product/users/')
		self.assertEquals(response1.status_code, 302)

		response2=self.client.get('/product/users/adduser/')
		self.assertEquals(response2.status_code, 302)
		print ">>>>ProductForm Validation Check<<<<"


class ViewsTest(TestCase):
	def setUp(self):
		self.client = Client()

		self.login_fields={'username':'Rama Krishna', 'password':'abcdefgh'}

	def test_login(self):
		login = Login(self.login_fields)
		self.assertTrue(login.is_valid())
		response=self.client.get('/product/')
		self.assertEquals(response.status_code, 200)
		response1=self.client.get('/product/users/')
		self.assertEquals(response1.status_code, 302)

		print ">>>>Views Testing<<<<"










# class CategorymodelTest(TestCase):

# 	def setUp(self):
# 		self.user=User.objects.create(name='rk', email='ramakrishna469@gmail.com')

# 	def test_cat(self):
# 		self.assertEquals(Category.objects.count(),0)
# 		cat=Category.objects.create(name="Mobile3")
# 		cat.user.add(self.user)
# 		self.assertEquals(Category.objects.count(),1)
# 		self.assertEquals(self.user, cat.user.all()[0])
# 		self.assertEquals(cat.cat_name(),"Mobile3")

# class testForms(TestCase):
# 	def setUp(self):
# 		self.user=User.objects.create(name='Rama Krishna', email='ramakrishna@micropyramid.com')
# 		self.data={'name':'RamaKrishna','email':'ramakrishna1@micropyramid.com'}
# 		self.cat={'name':'Mobile3','user':[self.user.id]}

# 	def test_userform(self):
# 		user=UserForm(self.data)
# 		self.assertEquals(user.is_valid(), True)

# 	def test_catform(self):
# 		ca=CategoryForm(self.cat)
# 		self.assertEquals(ca.is_valid(), True)

# 	def test_invalid(self):
# 		cat=CategoryForm(self.data2)
# 		self.assertFalse(cat.is_valid())

# class testViews(TestCase):
# 	def setUp(self):
# 		self.Client=Client()

# 	def test_simple(self):
# 		response=self.Client.get('/product/users/adduser/')
# 		self.assertEquals(response.status_code, 302)
# 	def test_simple1(self):
# 		self.assertEquals(User.objects.count(), 0)
# 		self.data={'name':'admin','email':'ramakrishna1@micropyramid.com'}
# 		response=self.Client.post('/product/users/adduser/',self.data)
# 		print response.status_code
# 		self.assertEquals(User.objects.count(), 1)