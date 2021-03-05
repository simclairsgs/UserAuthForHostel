from django.shortcuts import render,redirect
from django.http import HttpResponse,QueryDict,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Master_Db,Login_Auth_Db
from .serializers import Master_DbSerializer,Login_Auth_DbSerializer
from backend_Mp import settings


# Create your views here.
def index(request):
    return HttpResponse('<h1>Hai i am sk</h1>')


@api_view(['POST'])
def login_user(request):
    register_no = request.data.get("Register_No")
    otp = request.data.get('Otp')
    key = request.data.get('Key')
    print(register_no)
    if(key == settings.SECRET_KEY):
        try:

            register_num = Login_Auth_Db.objects.get(Register_No= register_no)
            
        except:
            return Response("Invalid userid")
        try:
            otpnum = Login_Auth_Db.objects.get(Otp = otp)
        except:
            return Response("Invalid Otp")
        print("hai")
        from random import randint
        create_random=(randint(10000000, 999999999))
        otpnum.Otp = create_random
        otpnum.save()
        
        profile = Master_Db.objects.get(Register_No = register_no)
        
        serializer = Master_DbSerializer(profile,many=False)
        
        return Response(serializer.data)
                

    else:
        return Response("Invalid Key")

