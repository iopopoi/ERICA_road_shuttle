def minute2time(minute):# 주어진 minute을 "00:00"의 형태로 출력해주는 함수
    hour=(int)(((minute-minute%60)/60)%24)
    mit=minute%60
    s_hour=str(hour)
    s_mit=str(mit)
    if(hour<10) : s_hour ="0"+s_hour
    if(mit<10) : s_mit ="0"+s_mit
    return s_hour+":"+s_mit

# print(minute2time(0)) issue사항 수정완료 코드
