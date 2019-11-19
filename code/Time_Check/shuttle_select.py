import os
from IsWeekend import IsWeekend
from tominute import Tominute


def shuttle_select(time, station):
    txt_path = os.path.dirname(__file__) #현재 경로 저장

    if IsWeekend() == False: #평일일때
        if station == "shuttlecok_to_sub": #도착지가 한대앞일때
            txt_path = os.path.join(txt_path,"shuttlecok_to_subwaystation_weekday.txt") #텍스트 위치 경로에 추가
        elif station == "shuttlecok_to_dom":
            txt_path = os.path.join(txt_path,"shuttlecok_to_dom_weekday.txt") #텍스트 위치 경로에 추가
        else:
            #txt_path = os.path.join(txt_path,"dom_to_shuttlecok_weekday.txt") #텍스트 위치 경로에 추가
            return -1
    else:
        if station == "shuttlecok_to_sub": #도착지가 한대앞일때
            txt_path = os.path.join(txt_path,"shuttlecok_to_subwaystation_weekend.txt") #텍스트 위치 경로에 추가
        elif station == "shuttlecok_to_dom":
            txt_path = os.path.join(txt_path,"shuttlecok_to_dom_weekend.txt") #텍스트 위치 경로에 추가
        else:
            #txt_path = os.path.join(txt_path,"dom_to_shuttlecok_weekend.txt") #텍스트 위치 경로에 추가
            return -1
    

    infile = open(txt_path,"r") #파일 읽음
    text = infile.read()

    S = text.partition(":") 
    SS = S[2].partition(",")
    text = SS[2]
    chk_timetable = Tominute(int(S[0]),int(SS[0]))

    while(time>chk_timetable):
        S = text.partition(":")
        SS = S[2].partition(",")
        text = SS[2]
        chk_timetable = Tominute(int(S[0]),int(SS[0]))
        if text == "":
            return -1
        
    infile.close()
    return chk_timetable 

print(shuttle_select(2014,"shuttlecok"))
