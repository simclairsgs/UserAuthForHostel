from rest_framework import serialiizer
from .models import Master_Db

class Master_DbSerializer(serialiizer.Modelserializer):
    class Meta:
        model = Master_Db
        Fields = '__all__'
