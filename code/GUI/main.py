import math
from datetime import datetime, date, timedelta
import folium_draw_line
import tkinter as tk
from tkinter import font, ttk
import os
import webbrowser
import folium_search_spot
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))) + "\Time_Check")
import Dijkstra
from Date import *

window = tk.Tk()
window.title("ERICA Road Shuttle")
window.geometry('650x500+500+200')  # 창 크기, 위치
window.configure(background='White')  # 바탕 색


#장소검색 버튼을 누르면 실행되는 함수
def view_map_B_event():
    folium_search_spot.make_html()
    url = os.path.abspath("")
    url = os.path.join(url, "spot_search.html")

    webbrowser.open(url)

#go to check버튼을 누르면 실행되는 함수
def open_html():
    url = os.path.abspath("")
    url = os.path.join(url, "path_line.html")
    webbrowser.open(url)


#Search버튼을 누르면 실행되는 함수
def View_path():
    start = start_point.get()
    end = end_point.get()
    if start == "출발지 선택":
        return False
    if end == "도착지 선택":
        return False

    (arrival_time, path_list) = Dijkstra.dijkstra(start, end)
    folium_draw_line.draw_path(path_list)

    # 도착시간을 알려주는 label 추가
    arrive_time = math.ceil(arrival_time)
    hour = (arrive_time-arrive_time % 60)/60
    arrive_time = deltaTime(hour, arrive_time % 60, 0)
    arrival_text = "도착 예정 시간은 " + \
        str(arrive_time.hour)+"시 "+str(arrive_time.minute)+"분 입니다."
    arrive_label = tk.Label(window, text=arrival_text, bg="white",
                            width=32, height=1, font=("맑은 고딕", 15),  bd=1)
    arrive_label.place(x=162, y=240)

    # 경로를 알려주는 web을 여는 버튼 추가
    way = tk.Button(window, text="!! Go To Check !!", font=(
        "맑은 고딕", 15), relief="solid", fg='Green', bg='white', width=25, height=1, command=open_html)
    way.place(x=200, y=300)


#장소검색 버튼
font = tk.font.Font(family="맑은 고딕", size=16, weight='bold')  # 폰트
view_map_B = tk.Button(window, text="장소 검색", font=font, fg='White', bg='green',
                       command=view_map_B_event)
view_map_B.place(x=210, y=100, width=265, height=50)  # 라벨 위치 및 크기


#출도착지 선택 콤보박스
values = ['셔틀콕', '제1공학관', '제3공학관', '제4공학관',
          '제1학술관', '컨퍼런스홀', '제2과학기술관', '학생복지관',
          '학생회관', '학술정보관', '제5공학관', '창업보육센터',
          '학연산 클러스터', '기숙사 셔틀콕','한대앞역']
start_point = tk.ttk.Combobox(window, height=20, width=10, values=values)
start_point.place(x=210, y=190)
start_point.set("출발지 선택")

end_point = tk.ttk.Combobox(window, height=20, width=10, values=values)
end_point.place(x=310, y=190)
end_point.set("도착지 선택")


#search 버튼
font = tk.font.Font(family="맑은 고딕", size=10, weight='bold')
search = tk.Button(window, text="SEARCH!", font=font,
                   fg='White', bg='Red', command=View_path)
search.place(x=410, y=185)

tk.mainloop()
