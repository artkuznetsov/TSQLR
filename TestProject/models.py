from django.db import models
from django.utils import timezone


class Category(models.Model):
	NameClass = models.CharField(max_length = 20)
	def __str__(self):
		return self.NameClass

class Quest(models.Model):
	NameQuest = models.CharField(max_length = 20)
	QuestText = models.TextField()
	WTask = models.TextField()
	Category = models.ForeignKey('Category')
	Weight = models.IntegerField()
	def __str__(self):
		return self.NameQuest

"""
class Person(models.Model):
	FirstName = models.CharField(max_length = 20)
	SecondName = models.CharField(max_length = 20)
	Group = models.CharField(max_length = 10)
	def __str__(self):
		return self.FirstName
"""
class ConnectDateBase(models.Model):
	NameConnection = models.CharField(max_length = 10)
	ConnectionString = models.TextField()
	def __str__(self):
		return self.NameConnection

class Test(models.Model):
	Name = models.CharField(max_length = 30)
	DateActivate = models.DateTimeField()
	Time = models.IntegerField()
	Quest = models.ManyToManyField('Quest')
	TestPerson = models.ManyToManyField('auth.user', through = 'TestPerson')
	def __str__(self):
		return self.Name

class TestPerson(models.Model):
	Person = models.ForeignKey('auth.user')
	Test = models.ForeignKey(Test)
	Mark = models.IntegerField()
	StartTest = models.DateTimeField()

