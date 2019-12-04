import heapq
from spot import *
# 셔틀시간을 확인하는 기능 미완성
def Dijkstra(station, destination):
    heap =[]
    building=[1,2,23,15,17,24,16,14,13,19,29,35,38,33]
    visit = [ 0 for i in range(50)]
    visit_from = [ 0 for i in range(50)]
    heapq.heappush(heap,( 0 , (station , station) ) )
    visit_from[station]=station
    while heap is not None:
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
                if building.count(next) > 0 and next != destination:
                    heapq.heappush( heap, (cnt + tpl[1] +1, (next , vtx)))
                else :    
                    heapq.heappush( heap, (cnt + tpl[1], (next , vtx)))
    spot_load = []
    s = destination
    while visit_from[s] != s :
        spot_load.append(s)
        s=visit_from[s]
    spot_load.append(station)
    spot_load.reverse()
    return cnt, spot_load

print(Dijkstra(33,1))
print(Dijkstra(26,20))
