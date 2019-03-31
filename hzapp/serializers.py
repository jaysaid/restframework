from django.contrib.auth.models import User
from hzapp.models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields =('id','username','password','first_name','last_name','email')

