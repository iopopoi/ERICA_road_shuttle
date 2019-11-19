import os
from Date import *

def Find_txt_path(time, station, destination):
    txt_path = os.path.dirname(__file__) #현재 경로 저장
    txt_path = os.path.join(txt_path,"timetable")
    
    if IsWeekend(time) == False: # 평일일 때
        if station == "shuttlecok": #셔틀콕 출발
            if destination == "subwaystation":#한대앞 도착
                txt_path = os.path.join(txt_path,"shuttlecok_to_subwaystation_weekday.txt") #텍스트 위치 경로에 추가
            elif destination == "dom": #긱사 도착
                txt_path = os.path.join(txt_path,"shuttlecok_to_dom_weekday.txt") #텍스트 위치 경로에 추가
            else:
                #txt_path = os.path.join(txt_path,"dom_to_shuttlecok_weekday.txt") #텍스트 위치 경로에 추가
                return -1

    else: # 주말일 때
        if station == "shuttlecok": #셔틀콕 출발
            if destination == "subwaystation": #한대앞 도착
                txt_path = os.path.join(txt_path,"shuttlecok_to_subwaystation_weekend.txt") #텍스트 위치 경로에 추가
            elif destination == "dom": #긱사 도착
                txt_path = os.path.join(txt_path,"shuttlecok_to_dom_weekend.txt") #텍스트 위치 경로에 추가
            else:
                #txt_path = os.path.join(txt_path,"dom_to_shuttlecok_weekend.txt") #텍스트 위치 경로에 추가
                return -1
    
    return txt_path


def shuttle_select(time, station, destination):
    txt_path = Find_txt_path(time,station,destination) #타야하는 셔틀시간표 경로 찾음
    infile = open(txt_path,"r") #파일 읽음
    text = infile.read()

    S = text.partition(":")
    SS = S[2].partition(",") 
    text = SS[2] # 
    
    shuttle_time = make_time(int(SS[0]),int(S[0]),time)

    while(Tominute(time) > Tominute(shuttle_time)): # 분으로 환산하여 비교 후 이미 떠난 셔틀이면 패스
        S = text.partition(":")
        SS = S[2].partition(",")
        text = SS[2]

        shuttle_time = make_time(int(SS[0]),int(S[0]),time) #셔틀 시간을 날짜 형식으로 바꿈

        if text == "": #모든 셔틀이 떠나갔으면
            return -1
        
    infile.close()
    return shuttle_time

print(shuttle_select(now(),"shuttlecok","subwaystation"))