from django.shortcuts import render,redirect
from django.http import HttpResponse,QueryDict,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Master_Db,Login_Auth_Db,Today_Attendance_Db
from .serializers import Master_DbSerializer,Login_Auth_DbSerializer,Today_Attendance_DbSerializer
from backend_Mp import settings
from . import tests
from .import automatedTasks
from datetime import datetime,date
from pytz import timezone
IST = timezone('Asia/Kolkata')


automatedTasks.main()

def index(request):
    return HttpResponse('<h1>You are Successfully connected to the Authentication Network.</h1>')


@api_view(['POST'])
def login_user(request):
    register_no = request.data.get("Register_No")
    otp = request.data.get('Otp')
    key = request.data.get('Key')
    if key == settings.SECRET_KEY or tests.TEST_MODE :
        try:
            register_num = Login_Auth_Db.objects.get(Register_No= register_no)
            if otp == register_num.Otp :
                if tests.TEST_MODE:
                    register_num.Otp = 123456
                    register_num.save()
                else:
                    from random import randint
                    create_random=(randint(10000000, 999999999))
                    register_num.Otp = create_random
                    register_num.save()
            else:
                return Response({"Error":"InvalidOtp"})    
        except:
            return Response({"Error":"InvalidUserId"})

        profile = Master_Db.objects.get(Register_No = register_no)
        serializer = Master_DbSerializer(profile,many=False)
        return Response(serializer.data)
    else:
        return Response({"Error":"InvalidKey"})


@api_view(['POST'])
def CheckAuthStatus(request):
    register_no = request.data.get("Register_No")
    key = request.data.get('Key')
    if key == settings.SECRET_KEY or tests.TEST_MODE:
        try:
            data = Today_Attendance_Db.objects.get(Register_No = register_no)
            now = datetime.now(IST)
            if now.hour > tests.AUTH_ALLOW_START and now.hour<tests.AUTH_ALLOW_END:
                if data.Auth_Status:
                    return Response({"Status":data.Auth_Status,"Allow_auth":False})
                else:
                    return Response({"Status":data.Auth_Status,"Allow_auth":True})
            else:
                return Response({"Status":data.Auth_Status,"Allow_auth":False})
        except:
            return Response({"Error":"ERR-CODE-404"})
    else:
        return Response({"Error":"InvalidKey"})


@api_view(['POST'])
def authUser(request):
    register_no = request.data.get("Register_No")
    key = request.data.get('Key')
    if key == settings.SECRET_KEY or tests.TEST_MODE:
        try:
            data = Today_Attendance_Db.objects.get(Register_No = register_no)
            data.Auth_Status = True
            data.Auth_Time = datetime.now(IST)
            data.Date = date.today()
            data.save()
            return Response({"Status":"success"})
        except:
            return Response({"Error":"ERR-CODE-403","Status":"failed"})
    else:
        return Response({"Error":"InvalidKey"})
