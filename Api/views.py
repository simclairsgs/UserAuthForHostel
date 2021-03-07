from django.shortcuts import render,redirect
from django.http import HttpResponse,QueryDict,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Master_Db,Login_Auth_Db
from .serializers import Master_DbSerializer,Login_Auth_DbSerializer
from backend_Mp import settings
from . import tests

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

