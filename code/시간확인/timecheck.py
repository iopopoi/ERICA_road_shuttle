def timecheck(time):
    infile=open("time_shuttle.txt","r")
    chk_timetable=0
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

print(timecheck(889))