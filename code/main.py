from search import search_road
from Time_Check import Date 

class INPUT_ERROR(Exception): pass

#입력
while True:
    try:
        start_point = int(input("출발지를 입력해주세요 : ")) #출발지를 장소마다 매겨진 번호로 입력
        if start_point < 1 and start_point > 20:
            raise INPUT_ERROR

    except INPUT_ERROR:
        print("1~20까지의 숫자를 입력해주세요")
    
    except: pass
    else: break

while True:
    try:
        end_point = int(input("도착지를 입력해주세요 : ")) #도착지를 장소마다 매겨진 번호로 입력
        if end_point < 1 and end_point > 20:
            raise INPUT_ERROR

    except INPUT_ERROR:
        print("1~20까지의 숫자를 입력해주세요")
    
    except: pass
    else: break

#도착 예정 시간 구하기
ans = search_road(Date.now(), start_point, end_point)


#출력
print("도착 예정 시간은",end = " ")
print(ans, end = " ")
print("입니다")


