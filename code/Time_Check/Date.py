#날짜를 계산하는 함수가 들어있는 모듈

from datetime import datetime, date, timedelta

def today(): #오늘 날짜를 리턴
    return datetime.today()

def deltaday(delta, start_day = -1): #특정 날짜에서 몇일 후,전의 날짜를 리턴
    if start_day == -1: #디폴트 값은 오늘 날짜
        start_day = today()
    return start_day + timedelta(delta)

#오늘 날짜를 입력받아 주말인지 판단하는 함수
def IsWeekend(time = -1):
    if time == -1: # 디폴트 값이면 오늘 날짜로
        time = today()

    week = time.weekday() #현재 시간을 불러옴
    if week == 5 or week == 6: #토요일이거나 일요일이면 참
        return True
    else:
        return False
