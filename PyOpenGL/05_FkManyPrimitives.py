from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import QPainter, QPen
from PyQt6 import *

import sys


# 정점 데이터 (2차원 정점을 리스트로 표현하고, 이들의 리스트로 복수의 정점 관리)
POINTS = [[0, 0], [10, 10], [100, 50]]


class MyWindow(QMainWindow) :
    def __init__(self, title = "") :
        QMainWindow.__init__(self)
        self.setWindowTitle(title)

        # GUI설정
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        gui_layout = QHBoxLayout() # CentralWidget의 수평 나열 레이아웃

        # 배치될 것을 - 정점 입력을 받기 위한 위짓
        central_widget.setLayout(gui_layout)

        self.controlGroup = QGroupBox("정점 입력")
        gui_layout.addWidget(self.controlGroup)

        control_layout = QVBoxLayout()
        self.controlGroup.setLayout(control_layout)

        ## 정점을 초기화하는 버튼 추가
        ## 이 버튼을 누르면 resetPoints라는 메소드 호출
        reset_button = QPushButton("정점 초기화", self)
        reset_button.clicked.connect(self.resetPoints)

        control_layout.addWidget(reset_button)

        ## 정점을 입력받기 위한 위짓 만들고, poinInput이라는 멤버로 관리
        self.poinInput = Drawer(parent = self)
        gui_layout.addWidget(self.poinInput)

    def resetPoints(self, btn) :
        global POINTS
        POINTS = []
        self.poinInput.update()

class Drawer(QWidget) :
    def __init__(self, parent = None) :
        QWidget.__init__(self, parent)
        self.parent = parent
        # QPainter 멤버 준비
        self.painter = QPainter()

    # QPainter를 이용하여 입력된 정점을 출력
    def paintEvent(self, event) :
        global POINTS

        self.painter.begin(self)

        # 점찍기!
        self.painter.setPen(QPen(Qt.GlobalColor.red, 6))
        for i in range(len(POINTS)) :
            self.painter.drawPoint(QPointF(POINTS[i][0], POINTS[i][1]))
        
        
        # 점과 점사이 그림그리기!
        self.painter.setPen(QPen(Qt.GlobalColor.blue, 2))
        for i in range(len(POINTS) - 1) :
            # POINTS의 [i]번째 [x, y]
            self.painter.drawLine(QLineF(POINTS[i][0], POINTS[i][1],
            POINTS[i + 1][0], POINTS[i+1][1]))
        
        self.painter.end()
    
    # 정점 입력하는 방법으로 마우스 이벤트 발생시에 좌표를 읽어
    # 이 정점을 표현하는 2차우너 정보를 리스트로 만들어 정점 리스트 POINTS에 추가
    def mousePressEvent(self, event) :
        POINTS.append([event.position().x(), event.position().y()])
        print(event.position().x(), event.position().y())
        self.update()

def main(argv = []) :
    app = QApplication(argv)
    window = MyWindow("데이터 입력")
    window.setFixedSize(800, 400)
    window.show()
    app.exec()

if __name__ == "__main__" :
    main(sys.argv)
    
