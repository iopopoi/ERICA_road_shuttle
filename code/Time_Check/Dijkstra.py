import heapq
from spot import *
from Date import *
from shuttle_select import *
from datetime import datetime, date, timedelta


# 셔틀콕을 탈 경우에 거치는 경로 추가
def plus_shuttle_road(spot_list):
    bus = [12,43,38]
    start_bus = -1
    end_bus = -1
    for i in range(0,len(spot_list)-1):
        if i+1 < len(spot_list) and (spot_list[i] in bus) and (spot_list[i+1] in bus):
            if start_bus == -1:
                start_bus = i
            end_bus = i+1
        
    if start_bus != -1 and end_bus != -1:
        if end_bus < len(spot_list):
            spot_list = spot_list[:start_bus] + [0] + spot_list[start_bus:end_bus+1] + [0] + spot_list[end_bus+1:]
        else:
            spot_list =  spot_list[:start_bus] + [0] + spot_list[start_bus:end_bus+1] + [0]
    

    n=len(spot_list)
    for i in range(1,n,1):
        if spot_list[i-1]==12 and spot_list[i]==38:
            spot_list=spot_list[:i]+[78,37,76,77]+spot_list[i:]
        elif spot_list[i-1]==38 and spot_list[i]==12:
            spot_list=spot_list[:i]+[77,76,37,78]+spot_list[i:]
    return spot_list
    
    

def dijkstra(start_point, end_point):
    station = D_building[start_point]
    destination = D_building[end_point]

    heap =[]
    visit = [ 0 for i in range(80)]
    visit_from = [ 0 for i in range(80)]
    heapq.heappush(heap,( 0 , (station , station) ) )
    visit_from[station]=station
    while heap != []:
        vtx = heap[0][1][0]
        cnt = heap[0][0]
        x=heap[0][1][1]
        heapq.heappop(heap)
        if visit[vtx]:continue
        visit_from[vtx]=x
        visit[vtx]=1
        if vtx == destination : break
        for tpl in spot_list[vtx] :
            next= tpl[0]
            if  visit[next] == 0 :
                if (vtx ==12 or vtx==38 or vtx ==43) and (next == 12 or next == 38 or next == 43):
                    time = deltaTime(((cnt-cnt%60)/60)%24,cnt%60,0)
                    if vtx == 12:
                        sstation = "셔틀콕"
                        if next == 43:
                            ddestination = "한대앞역"
                        elif next == 38:
                            ddestination = "기숙사 셔틀콕"
                    elif vtx == 38:
                        sstation = "기숙사 셔틀콕"
                        if next == 12:
                            ddestination = "셔틀콕"
                    elif vtx == 43:
                        sstation = "한대앞역"
                        if 12:
                            ddestination = "셔틀콕"
                    shuttle_time = shuttle_select(time, sstation, ddestination)
                    shuttle_time = Tominute(shuttle_time)-Tominute(now())
                    heapq.heappush( heap, ( shuttle_time+tpl[1] , (next , vtx) ) )
                else :    
                    heapq.heappush( heap, (cnt + tpl[1], (next , vtx)))
    spot_load = []
    s = destination
    while visit_from[s] != s :
        spot_load.append(s)
        s=visit_from[s]
    spot_load.append(station)
    spot_load.reverse()
    spot_load=plus_shuttle_road(spot_load)
    return cnt, spot_load
