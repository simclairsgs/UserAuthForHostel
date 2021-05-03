'''
Copyright (C) 2021 , George Simclair Sam 

This file is part of the UserAuthForHostel project.

This file can not be copied and/or distributed without the express
permission of George Simclair Sam, simclair.sgs@gmail.com .
'''
from apscheduler.schedulers.background import BackgroundScheduler
from .import tests

def reset_auth_db():
    print('>>> Reset Auth DB task started... <<<')
    from .models import Today_Attendance_Db
    from datetime import date,timedelta
    from djqscsv import write_csv
    obj = Today_Attendance_Db.objects.all()
    with open('./attendance_log/'+str(date.today()-timedelta(days=1))+'.csv', 'wb') as csv_file:
        write_csv(obj, csv_file)
    obj.update(Auth_Status=False,Auth_Time='Not Auth',Date=date.today())
    print(">>> Reset Auth DB task ended... <<<")
    pass

# CHANGE AUTHENTICATION TIME SLOT AND REPORT TIME IN tests.py

def main():
    scheduler = BackgroundScheduler(timezone="Asia/kolkata")    #To change Timezone change here
    print("Automated tasks init...")
    scheduler.add_job(reset_auth_db,'cron',hour=tests.RST_DB_GEN_RPRT_TIME)
    scheduler.start()



