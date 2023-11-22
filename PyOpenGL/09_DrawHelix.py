import typing
from OpenGL.GL import *
from OpenGL.GLU import *

import sys

from PyQt6.QtCore import *

from PyQt6.QtWidgets import *
from PyQt6.QtOpenGLWidgets import *

import math

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

def DrawBox(l, r, b, t, n, f) : #glOrth가 만드는 공간(육면체) 가시화
    glColor3f(1, 1, 1)
    glBegin(GL_LINE_LOOP)
    #앞면
    glVertex3f(l, t, -n)
    glVertex3f(l, b, -n)
    glVertex3f(r, b, -n)
    glVertex3f(r, t, -n)
    glEnd()

    glBegin(GL_LINE_LOOP)
    #뒷면
    glVertex3f(l, t, -f)
    glVertex3f(l, b, -f)
    glVertex3f(r, b, -f)
    glVertex3f(r, t, -f)
    glEnd()


class MyGLWidget(QOpenGLWidget) :
    left = bottom = near = -2
    right = top = far = 2
    
    def __init__(self, parent = None, observation = False) :
        super().__init__(parent)
        self.observation = observation

    def initializeGL(self) :
        pass

    def resizeGL(self, w, h) :
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        
        if self.observation :
            glOrtho(-4, 4, -4, 4, -100, 100)
        else :
            glOrtho(self.left, self.right, self.bottom, self.top, self.near, self.far)

    def paintGL(self) :
        glMatrixMode(GL_PROJECTION) ##투상 좌표계(GL_PROJECTION) 의 공간을 앞으로 계산하겠다는 뜻입니다.
                                    ##투상을 표현하기 전에 선언합니다.
        glLoadIdentity()            ##좌표계 초기화
        if self.observation == True :
            glOrtho(-4, 4, -4, 4, -100, 100)
        else :
            glOrtho(self.left, self.right, self.bottom, self.top, self.near, self.far)

        glMatrixMode(GL_MODELVIEW) ##모델 좌표계와 시점 좌표계(GL_MODELVIEW) 의 공간을 앞으로 계산하겠다는 뜻입니다.
                                   ##사물, 시점을 표현하기  전에 선언합니다.
        glLoadIdentity()
        if self.observation == True :
            gluLookAt(1, 1, 0.5, 0, 0, 0, 0, 1, 0)
        DrawAxes()
        DrawHelix()
        DrawBox(self.left, self.right, self.bottom, self.top, self.near, self.far)



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
        self.glWidget2 = MyGLWidget(observation = True) # 관측용 OpenGL 위짓

        gui_layout.addWidget(self.glWidget1)
        gui_layout.addWidget(self.glWidget2)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key.Key_A:
            MyGLWidget.left -= 0.1
        elif e.key() == Qt.Key.Key_S:
            MyGLWidget.left += 0.1
        elif e.key() == Qt.Key.Key_D:
            MyGLWidget.right -= 0.1
        elif e.key() == Qt.Key.Key_F:
            MyGLWidget.right += 0.1
        elif e.key() == Qt.Key.Key_Q:
            MyGLWidget.top += 0.1
        elif e.key() == Qt.Key.Key_W:
            MyGLWidget.top -= 0.1
        elif e.key() == Qt.Key.Key_Z:
            MyGLWidget.near += 0.1
        elif e.key() == Qt.Key.Key_X:
            MyGLWidget.near -= 0.1
        elif e.key() == Qt.Key.Key_V:
            MyGLWidget.far += 0.1
        elif e.key() == Qt.Key.Key_C:
            MyGLWidget.far -= 0.1

        self.glWidget1.update()
        self.glWidget2.update()
    

def main(argv = sys.argv) :
    app = QApplication(argv)
    window = MyWindow("glOrtho 관측한다!")
    window.setFixedSize(1200, 600)
    window.show()
    app.exec()

if __name__ == "__main__" :
    main(sys.argv)
