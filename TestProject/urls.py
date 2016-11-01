from django.conf.urls import url, include

import TestApp
import TestProject
from . import views

urlpatterns = [
  url(r'^$', TestProject.views.home),
  url(r'^users/(?P<LoginUser>[^/]+)/profile$', views.TestsUser, name='TestUser'),
]