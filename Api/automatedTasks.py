from .models import Today_Attendance_Db
import datetime

def reset_auth_db():
    print('>>> Reset Auth DB task started... <<<')
    obj = Today_Attendance_Db.objects.all()
    from djqscsv import write_csv
    with open('./attendance_log/'+datetime.datetime.today+'.csv', 'wb') as csv_file:
        write_csv(obj, csv_file)
    obj.update(Auth_Status=False,Auth_Time='Not Auth',Date=datetime.date.today() + datetime.timedelta(days=1))
    pass

def all_tasks():
    now = datetime.datetime.now()
    if(now.hour+5 == 24):
        reset_auth_db()
    else:
        print("Hourly Test...Done...")


