#from django.http import HttpResponse
#from django.shortcuts import render_to_response
from .forms import *
from .models import *
from django.http import *
from django.shortcuts import *




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
	try:
		user = auth.user.objects.get(username = LoginUser)
	except:
		HttpResponseNotFound("Not found!")
	try:
		UserTest = TestPerson.objects.filter(id = user.id).values()
	except:
		return HttpResponseServerError("Server error")	
	TestUser = []
	try:
		for test in UserTest:
			TestUser.append(Test.objects.values("id", "Name", "DateActivate", "Time").get(id = test["test_id"]))
	except:
		HttpResponseNotFound("Not found")
	return render(HttpRequest, "TestProject/profile.html",
                  {
                      "TestUser": TestUser
                  })

					
