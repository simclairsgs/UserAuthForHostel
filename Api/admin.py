'''
Copyright (C) 2021 , George Simclair Sam 

This file is part of the UserAuthForHostel project.

This file can not be copied and/or distributed without the express
permission of George Simclair Sam, simclair.sgs@gmail.com .
'''
from django.contrib import admin
from .models import Master_Db,Login_Auth_Db,Today_Attendance_Db
# Register your models here.
class Master_DbAdmin(admin.ModelAdmin):
    list_display = ['Register_No','Name','Room_No','Mobile_No','Parent_No','Email','Year','Department','Class','Father_Name','Gender','Date_of_birth']

class Login_Auth_DbAdmin(admin.ModelAdmin):
    list_display = ['Register_No','Otp']

class Today_Attendance_DbAdmin(admin.ModelAdmin):
    list_display = ['Register_No','Auth_Status','Auth_Time','Date']


admin.site.register(Master_Db, Master_DbAdmin)
admin.site.register(Login_Auth_Db,Login_Auth_DbAdmin)
admin.site.register(Today_Attendance_Db,Today_Attendance_DbAdmin)
