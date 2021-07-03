'''
Copyright (C) 2021 , George Simclair Sam 

This file is part of the UserAuthForHostel project.

This file can not be copied and/or distributed without the express
permission of George Simclair Sam, simclair.sgs@gmail.com .
'''

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
