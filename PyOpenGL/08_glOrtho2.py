from OpenGL.GL import *
from OpenGL.GLU import *

from PyQt6.QtWidgets import *
from PyQt6.QtOpenGLWidgets import *

import sys


class MyGLWidget(QOpenGLWidget) :
    def __init__(self):
        super().__init__()

    def initializeGL(self) :
        pass

    def resizeGL(self, w, h):
        pass

    def paintGL(self):
        pass

class MyWindow(QMainWindow) :
    def __init__(self, title = "머임") :
        super().__init__()
        self.setWindowTitle(title)

        ## GUI 설정
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        gui_layout = QHBoxLayout() # layout == 배치

        central_widget.setLayout(gui_layout)

        self.glWidget1 = MyGLWidget()
        self.glWidget2 = MyGLWidget()

        gui_layout.addWidget(self.glWidget1)
        gui_layout.addWidget(self.glWidget2)


def main(argv = sys.argv) :
    app = QApplication(argv)
    window = MyWindow("Tlqkf?")
    window.setFixedSize( 1200, 600)
    window.show()
    app.exec()

if __name__ == "__main__" :
    main(sys.argv)