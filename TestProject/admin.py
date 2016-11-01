from django.contrib import admin
from .models import Quest,Category,Person,Test,TestPerson,Group,ConnectDateBase

admin.site.register(Quest)
admin.site.register(Category)
admin.site.register(Person)
admin.site.register(Test)
admin.site.register(ConnectDateBase)
admin.site.register(Group)
