from apscheduler.schedulers.background import BackgroundScheduler


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

'''
def all_tasks():
    now = datetime.datetime.now()
    if(now.hour+5 == 24):
        reset_auth_db()
    else:
        print("Hourly Test...Done...")
'''

def main():
    scheduler = BackgroundScheduler(timezone="Asia/kolkata")
    print("Automated tasks init...")
    scheduler.add_job(reset_auth_db,'cron',hour=0)
    scheduler.start()



