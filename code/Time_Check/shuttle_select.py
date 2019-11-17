import os
from IsWeekend import IsWeekend

def shuttle_select(time, station):
    txt_path = os.path.dirname(__file__) #현재 경로 저장

    if IsWeekend() == False: #평일일때
        if station == "shuttlecok": #탑승 위치가 셔틀콕이면
            txt_path = os.path.join(txt_path,"shuttlecok_to_subwaystation_weekday.txt") #텍스트 위치 경로에 추가

    else:
        return -1 #아직 셔틀시간표 미완으로 남겨둠
    

    infile=open(txt_path,"r") #파일 읽음
    text=infile.read()

    S=text.partition(":") 
    SS=S[2].partition(",")
    text=SS[2]
    chk_timetable=int(S[0])*60+int(SS[0])

    if time>1380 :
         chk_timetable=2000

    while(time>chk_timetable):
        S=text.partition(":")
        SS=S[2].partition(",")
        text=SS[2]
        chk_timetable=int(S[0])*60+int(SS[0])
        
    infile.close()
    return chk_timetable 

print(shuttle_select(2012,"shuttlecok"))