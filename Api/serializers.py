from rest_framework import serializers
from .models import Master_Db,Login_Auth_Db,Today_Attendance_Db

class Master_DbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master_Db
        fields = '__all__'
        

class Login_Auth_DbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login_Auth_Db
        fields = '__all__'

class Today_Attendance_DbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Today_Attendance_Db
        fields = '__all__'
