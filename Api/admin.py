from django.contrib import admin
from .models import Master_Db
# Register your models here.
class Master_DbAdmin(admin.ModelAdmin):
    list_display = ['Register_No','Name','Room_No','Mobile_No','Parent_No','Email','Year','Department','Class','Father_Name','Genter','Date_of_birth']


admin.site.register(Master_Db, Master_DbAdmin)
