#날짜를 계산하는 함수가 들어있는 모듈

from datetime import datetime, date, timedelta
#date:날짜 저장 // datetime:날짜+시간 저장
#timedelta:특정 시각에 일정 시간을 더하거나 빼는 역할을 수행 / ex ) datetime.now() - timedelta(hours=3)

def now(): #지금 날짜 및 시간을 리턴 2019-11-19 06:29 형식
    return datetime.today()


def deltaminute(delta, start_time = -1): #특정 날짜에서 몇 분 전, 후의 날짜를 리턴
    if start_time == -1:
        start_time = now()
    return start_time + timedelta(minutes = delta)


def deltahour(delta, start_time = -1): #특정 날짜에서 몇 시간 전, 후의 날짜를 리턴 
    if start_time == -1:
        start_time = now()
    return start_time + timedelta(hours = delta)


def deltaday(delta, start_time = -1): #특정 날짜에서 몇일 전, 후의 날짜를 리턴
    if start_time == -1: #디폴트 값은 오늘 날짜
        start_time = now()
    return start_time + timedelta(delta)


def deltaTime(hour,minute,day, start_time = -1): #위의 3가지 함수를 통합한 함수
    if start_time == -1:
        start_time = now()
    return start_time + timedelta(hours = hour, minutes = minute, days= day)
    

def IsWeekend(time = -1): #오늘 날짜를 입력받아 주말인지 판단하는 함수
    if time == -1: # 디폴트 값이면 오늘 날짜로
        time = now().day

    week = time.weekday() #현재 시간을 불러옴
    if week == 5 or week == 6: #토요일이거나 일요일이면 참
        return True
    else:
        return False


def Tominute(time):#시간과 분을 분으로 환산해주는 함수
    return time.hour*60 + time.minute


def make_time(minute,hour,date = -1):#인자로 받은 값으로 날짜 형식의 자료 생성
    if date == -1 : # 디폴트 날짜는 오늘
        return datetime(now().year,now().month,now().day,hour,minute,0)
    else:
        return datetime(date.year,date.month, date.day,hour,minute,0)