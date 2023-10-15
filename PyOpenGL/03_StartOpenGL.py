from OpenGL.GL import *
from OpenGL.GLU import *

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtOpenGLWidgets import QOpenGLWidget

import sys

class MyGLWindow(QOpenGLWidget) : # QOpenGLWidet 상속
    def __init__(self, parent = None) :
        super(MyGLWindow, self).__init__(parent) # 슈퍼 클래스 QMainWindow생성자 실행
    """
     초기화initialize - OpenGL 콘텐츠의 초기화 콜백
     크기 변경resize - 윈도우가 생성되거나 크기가 변경될 때 호출되는 콜백
     디스플레이display - 화면에 그림을 그리는 일이 필요할 때 호출되는 콜백
    """
    def initializeGL(self) :
        glClearColor(0.1, 0.7, 0.3, 1.0)

    def resizeGL(self, w: int, h: int) :
        pass

    def paintGL(self) :

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        """
        GL_POINTS - 입력된 정점을 하나씩 점으로 가시화

        GL_LINES - 입력된 정점을 두 개씩 묶어 선분으로 표현

        GL_LINE_STRIP - 입력된 정점을 차례로 연결하여 하나의 폴리라인polyline 구성

        GL_LINE_LOOP - 입력된 정점을 차례로 연결한 뒤에 마지막 점을 시작점으로 연결

        GL_TRIANGLES - 입력된 정점을 세 개씩 묶어 삼각형을 그림

        GL_TRIANGLE_STRIP - 처음 세 정점으로 삼각형 그린 뒤,
         정점 추가될 때마다 삼각형을 직전 두 개 정점과 연결

        GL_TRIANGLE_FAN - 부채 모양으로 삼각형을 추가해 나감

        GL_QUADS - 정점 네 개씩을 묶어 사각형 그리기

        GL_QUAD_STRIP: 처음 네 개 정점으로 사각형 그리고,
         이후 두 개씩 묶어 직전 두 개 정점과 함께 사각형 그리기

        GL_POLYGON: 입력된 모든 정점으로 다각형을 그림
        """
        glBegin(GL_TRIANGLES)# 어떤 모양으로 그릴래?

        """
        정점 정보 제공 방법
        ix, iy, iz = -1, 0, 0
        fx, fy, fz = 1.0, 0.0, 0.0
        fverts = [fx-1.0, fy+1.0, fz]
        glBegin(GL_TRIANGLES)
        glVertex3i(ix, iy, iz)
        glVertex3f(fx, fy, fz)
        glVertex3fv(fverts)
        glEnd()
        """

        glColor3f(1, 1, 0)
        glVertex3f(-1, 0, 0)
        glVertex3f( 1, 0, 0)
        glVertex3f( 0, 1, 0)

        glColor3f(0, 1, 1)
        glVertex3f(-1, 0.5, 0)
        glVertex3f( 1, 0.5, 0)
        glVertex3f( 0,-0.5, 0)

        glEnd()

    

    
def main(argv = []) :
        app = QApplication(argv)
        window = MyGLWindow()
        window.setWindowTitle("Example1")
        window.setFixedSize(600, 600)
        window.show()
        sys.exit(app.exec())    

if __name__ == "__main__" :
    main(sys.argv)