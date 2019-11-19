#날짜를 계산하는 함수가 들어있는 모듈

from datetime import datetime, date, timedelta

def today(): #오늘 날짜를 리턴
    return datetime.today()

def deltaday(delta, start_day = -1): #특정 날짜에서 몇일 후,전의 날짜를 리턴
    if start_day == -1: #디폴트 값은 오늘 날짜
        start_day = today()
    return start_day + timedelta(delta)
