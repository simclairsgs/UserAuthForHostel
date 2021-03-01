from rest_framework import serializers
from .models import Master_Db,Login_Auth_Db

class Master_DbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master_Db
        Fields = '__all__'

class Login_Auth_DbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login_Auth_Db
        Fields = '__all__'