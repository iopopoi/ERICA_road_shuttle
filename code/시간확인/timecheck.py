import os

def timecheck(time):
    now_path = os.path.dirname(__file__)
    shuttle_time_path = os.path.join(now_path,"time_shuttle.txt")

    infile=open(shuttle_time_path,"r")
    text=infile.read()
    S=text.partition(":")
    SS=S[2].partition(",")
    text=SS[2]
    chk_timetable=int(S[0])*60+int(SS[0])
    if time>1380 : chk_timetable=2000
    while(time>chk_timetable):
        S=text.partition(":")
        SS=S[2].partition(",")
        text=SS[2]
        chk_timetable=int(S[0])*60+int(SS[0])
    infile.close()
    return chk_timetable 
