from PyQt5.QtWidgets import *
import sys


class My_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('test')
        self.move(700,300) # 스크린의 좌표
        self.resize(700,800) #스크린의 크기
        self.show() #위젯을 스크린에 띄우기
        

if __name__ == '__main__': # 현재 모듈의 이름이 __main__ 이라면
    app = QApplication(sys.argv)
    ex = My_Window()
    sys.exit(app.exec_())
