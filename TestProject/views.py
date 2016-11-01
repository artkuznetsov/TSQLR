#from django.http import HttpResponse
#from django.shortcuts import render_to_response
from .forms import *
from .models import *
from django.http import *
from django.shortcuts import *
from django.contrib.auth.models import User




def home(request):
    return render_to_response('TestProject/home.html')

def register(request):
    return render_to_response('registration/registration_form.html')

def login_page(request):
    return render_to_response('registration/login.html')

def logout_page(request):
    return render_to_response('registration/logout.html')

def registration_closed(request):
    return render_to_response('registration/registration_closed.html')

def registration_complete(request):
    return render_to_response('registration/registration_complete.html')


def PrimerTests(HttpRequest):
	try:
		tests = Test.objects.values("Name", "DateActivate", "Time")
	except:
		return HttpResponseServerError("Server error")
	return render(HttpRequest, "TestProject/tests.html",{"tests": tests})

def TestsUser(HttpRequest, LoginUser):
	user = User.objects.get(id = LoginUser)
	UserTest = TestPerson.objects.filter(Person = user)
	mass = []
	for i in UserTest:
		mass.append(Test.objects.get(id = i.Test_id))
	
	return render(HttpRequest, "TestProject/profile.html",
                  {
                      "TestUser": mass
                  })

					
