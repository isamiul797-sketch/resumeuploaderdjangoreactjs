from django.contrib import admin
from api.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name','email','dob','state','gender','location','pimg','rdoc']