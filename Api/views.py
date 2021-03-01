from django.shortcuts import render
from django.http import HttpResponse,QueryDict,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Master_Db,Login_Auth_Db
from .serializers import Master_DbSerializer,Login_Auth_Db 

# Create your views here.
def index(request):
    return HttpResponse('<h1>Hai i am sk</h1>')

@api_view(['POST'])
def login_user(request):
    register_no = request.data.get("Register_No")
    otp = request.data.get('Otp')
    try:
        register_num = Login_Auth_Db.objects.get(Register_No= register_no)
        print(register_num)
        return Response("succeses")
    except:
        print("fail")
        return Response("failed")
