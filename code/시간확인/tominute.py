# 현재 시간을 입력 받아 분으로 바꾸어주는 함수
from datetime import datetime

def Tominute():
    dminute=datetime.now().hour*60+datetime.now().minute
    return dminute 

print(Tominute())