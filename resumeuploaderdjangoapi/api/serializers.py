from rest_framework import serializers
from api.models import Profile

class ProfileSerializer(serializers.ModelField):
    class Meta:
        model = Profile
        fields = ['name','email','dob','state','gender','location','pimg','rdoc']