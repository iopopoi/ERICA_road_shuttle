#오늘 날짜를 입력받아 주말인지 판단하는 함수

from datetime import datetime

now = datetime.now()

def IsWeekend(date):
    week = datetime.today().weekday()
    if week == 5 or week == 6:
        return True
    else:
        return False


