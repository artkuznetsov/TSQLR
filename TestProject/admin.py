from django.contrib import admin
from .models import Category, Test, Quest, TestPerson

admin.site.register(Quest)
admin.site.register(Category)
admin.site.register(Test)
admin.site.register(TestPerson)
