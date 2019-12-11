import tkinter as tk
from tkinter import font,ttk
import os
import webbrowser
import folium_search_spot
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))) + "\Time_Check")
import Dijkstra
import folium_draw_line

window = tk.Tk()
window.title("ERICA Road Shuttle")
window.geometry('650x500+500+200')  # 창 크기, 위치
window.configure(background='White')  # 바탕 색


def view_map_B_event():
    folium_search_spot.make_html()
    url = os.path.abspath("")
    url = os.path.join(url, "spot_search.html")

    webbrowser.open(url)

def View_path():
    start = start_point.get()
    end = end_point.get()
    if start == "출발지 선택":
        return False
    if end == "도착지 선택":
        return False
    
    (arrival_time,path_list) = Dijkstra.dijkstra(start,end)
    print(path_list)
    folium_draw_line.draw_path(path_list)
    url = os.path.abspath("")
    url = os.path.join(url,"path_line.html")

    webbrowser.open(url)
    

#장소검색 버튼
font = tk.font.Font(family="맑은 고딕", size=15, weight='bold')  # 폰트
view_map_B = tk.Button(window, text="장소 검색", font=font, fg='White', bg='green',
                       command=view_map_B_event)
view_map_B.place(x=210, y=100, width=250, height=50)  # 라벨 위치 및 크기


#출도착지 선택 콤보박스
values = ['셔틀콕', '제1공학관', '제3공학관', '제4공학관',
          '제1학술관', '컨퍼런스홀', '제2과학기술관', '학생복지관',
          '학생회관', '학술정보관', '제5공학관', '창업보육센터',
          '학연산 클러스터', '기숙사 셔틀콕']
start_point = tk.ttk.Combobox(window, height=20, width = 10, values=values)
start_point.place(x=210, y=200)
start_point.set("출발지 선택")

values.append('한대앞역')
end_point = tk.ttk.Combobox(window, height=20, width = 10, values=values)
end_point.place(x=310, y=200)
end_point.set("도착지 선택")


#search 버튼
font = tk.font.Font(family="맑은 고딕", size = 10, weight='bold')
search = tk.Button(window,text="SEARCH!",font=font,fg='White',bg='Red',command=View_path)
search.place(x=410,y=195)

tk.mainloop()
