#오늘 날짜를 입력받아 주말인지 판단하는 함수
from Date import today
from datetime import datetime

def IsWeekend(time = -1):
    if time == -1: # 디폴트 값이면 오늘 날짜로
        time = today()

    week = time.weekday() #현재 시간을 불러옴
    if week == 5 or week == 6: #토요일이거나 일요일이면 참
        return True
    else:
        return False
