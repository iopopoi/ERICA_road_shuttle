import tkinter as tk
from tkinter import font
from tkinter import ttk
import os
import webbrowser
import folium_search_spot

window = tk.Tk()
window.title("ERICA Road Shuttle")
window.geometry('650x500+500+200')  # 창 크기, 위치
window.configure(background='White')  # 바탕 색


def view_map_B_event():
    folium_search_spot.make_html()
    url = os.path.abspath("")
    url = os.path.join(url, "spot_search.html")

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
start_point = tk.ttk.Combobox(window, height=20, values=values)
start_point.place(x=250, y=200)
start_point.set("           출발지 선택")

values.append('한대앞역')
end_point = tk.ttk.Combobox(window, height=20, values=values)
end_point.place(x=250, y=250)
end_point.set("           도착지 선택")


tk.mainloop()
