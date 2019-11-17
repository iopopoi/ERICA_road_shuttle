def minute2time(minute):
    hour=(int)(((minute-minute%60)/60)%24)
    mit=minute%60
    s_hour=str(hour)
    s_mit=str(mit)
    if(hour<10) : s_hour ="0"+s_hour
    if(mit<10) : s_mit ="0"+s_mit
    return s_hour+":"+s_mit

print(minute2time(0))
