import tkinter as tk
from tkinter import font
import os
import webbrowser

window = tk.Tk()
window.title("ERICA Road Shuttle")
window.geometry('650x500+500+200')  # 창 크기, 위치
window.configure(background='White')  # 바탕 색


def view_map_B_event():
    url = os.path.dirname(__file__)
    url = os.path.join(url,"example.html")

    webbrowser.open(url)


#장소검색 버튼
font = tk.font.Font(family="맑은 고딕", size=15, weight='bold')  # 폰트
view_map_B = tk.Button(window, text="장소 검색", font=font, fg='White', bg='green',
                       command=view_map_B_event)
view_map_B.place(x=210, y=100, width=250, height=50)  # 라벨 위치 및 크기


tk.mainloop()