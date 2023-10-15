from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWidgets import QLabel, QLineEdit, QVBoxLayout, QWidget

import sys

class MainWindow(QMainWindow) :
    def __init__(self) :
        # 슈퍼클래스의 초기화를 실행
        super().__init__()

        self.setWindowTitle("My App")
        
        # QLabel과 QLineEdit 클래스의 객체를 각각 생성한다
        self.label = QLabel()
        self.input = QLineEdit()

        # QLineEdit 객체의 값이 변경되면 QLablel로 전달된다
        self.input.textChanged.connect(self.label.setText)

        # 생성해 놓은 두 위짓 객체를 수직으로 배치할 레이아웃 객체 생성
        layout = QVBoxLayout()

        # 레이아웃 객체에 두 위짓 객체를 추가하여 감기게 한다
        layout.addWidget(self.label)
        layout.addWidget(self.input)

        # 윈도우에 표시될 위짓을 담는 컨테이너 객체 생성
        container = QWidget()

        # 컨테이너에 레이아웃 객체를 지정한다. 그 안에 담긴 위짓도 함께
        container.setLayout(layout)

        # 윈도우의 중심 위짓을 우리가 만든 것들이 담긴 컨테이너로 지정
        self.setCentralWidget(container)

app =QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()