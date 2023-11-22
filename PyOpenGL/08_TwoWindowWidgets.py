from OpenGL.GL import*
from OpenGL.GLU import*

from PyQt6.QtWidgets import*
from PyQt6.QtOpenGLWidgets import*

import math
import sys

def DrawAxes() :
    glBegin(GL_LINES)
    glColor3f(1,0,0)
    glVertex3f(0,0,0)
    glVertex3f(1,0,0)
    glColor3f(0,1,0)
    glVertex3f(0,0,0)
    glVertex3f(0,1,0)
    glColor3f(0,0,1)
    glVertex3f(0,0,0)
    glVertex3f(0,0,1)
    glEnd()

def DrawHelix() :
    glColor3f(1, 1, 1)
    glBegin(GL_LINE_STRIP)
    for i in range(1000) :
        angle = i / 10
        x, y = math.cos(angle), math.sin(angle)
        glVertex3f(x, y, angle / 10)
    glEnd()


class MyGLWidget(QOpenGLWidget) :
    def __init__(self, parent = None, observation = False) :
        super().__init__(parent)
        self.observation = observation

    def initializeGL(self) :
        pass

    def resizeGL(self, w, h) :
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

    def paintGL(self) :
        DrawAxes()
        DrawHelix()

class MyWindow(QMainWindow) :
    def __init__(self, title = "") :
        super().__init__()
        self.setWindowTitle(title)

        ##GUI 설정
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        ## 중심 위짓이 가질 레이아웃
        gui_layout = QHBoxLayout()
        central_widget.setLayout(gui_layout)

        self.glWidget1 = MyGLWidget()
        self.glWidget2 = MyGLWidget()

        gui_layout.addWidget(self.glWidget1)
        gui_layout.addWidget(self.glWidget2)

def main(argv = sys.argv) :
    app = QApplication(argv)
    window = MyWindow("glOrtho 관측한다!")
    window.setFixedSize(1200, 600)
    window.show()
    app.exec()

if __name__ == "__main__" :
    main(sys.argv)
