from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('login/',views.login_user,name="login"),
    path('check-status/',views.CheckAuthStatus,name="CheckAuth")

    

]