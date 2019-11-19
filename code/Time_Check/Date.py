#날짜를 계산하는 함수가 들어있는 모듈

from datetime import datetime, date, timedelta

def now(): #지금 날짜 및 시간을 리턴
    return datetime.today()


def deltaminute(delta, start_time = -1): #특정 날짜에서 몇 분 후, 뒤의 날짜를 리턴
    if start_time == -1:
        start_time = now()
    return start_time + timedelta(minutes = delta)


def deltahour(delta, start_time = -1): #특정 날짜에서 몇 시간 후, 뒤의 날짜를 리턴 
    if start_time == -1:
        start_time = now()
    return start_time + timedelta(hours = delta)


def deltaday(delta, start_time = -1): #특정 날짜에서 몇일 후,전의 날짜를 리턴
    if start_time == -1: #디폴d트 값은 오늘 날짜
        start_time = now()
    return start_time + timedelta(delta)


def IsWeekend(time = -1): #오늘 날짜를 입력받아 주말인지 판단하는 함수
    if time == -1: # 디폴트 값이면 오늘 날짜로
        time = today().day

    week = time.weekday() #현재 시간을 불러옴
    if week == 5 or week == 6: #토요일이거나 일요일이면 참
        return True
    else:
        return False


def minute2time(minute): # 주어진 minute을 "00:00"의 형태로 출력해주는 함수
    hour = (int)(((minute-minute%60)/60)%24)
    mit = minute%60
    s_hour = str(hour)
    s_mit = str(mit)

    if hour < 10 : 
        s_hour = "0" + s_hour
    if mit < 10 : 
        s_mit = "0" + s_mit

    return s_hour + ":" + s_mit


def Tominute(hour,minute): #시간과 분을 입력받아 분으로 바꾸는 함수
    return hour*60+minute

