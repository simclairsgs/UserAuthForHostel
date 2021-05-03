'''
Copyright (C) 2021 , George Simclair Sam 

This file is part of the UserAuthForHostel project.

This file can not be copied and/or distributed without the express
permission of George Simclair Sam, simclair.sgs@gmail.com .
'''

from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('login/',views.login_user,name="login"),
    path('check-status/',views.CheckAuthStatus,name="CheckAuth"),
    path('auth-user/',views.authUser,name="AuthUser")
    

]