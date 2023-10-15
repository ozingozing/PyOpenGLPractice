from OpenGL.GL import *
from OpenGL.GLU import *

import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtOpenGLWidgets import QOpenGLWidget

class MyGLWindow(QOpenGLWidget) :
    def __init__(self, parent = None) :
        super(MyGLWindow, self).__init__(parent)

    def initializeGL(self) :
        #OpenGL 그리기를 수행하기 전에 각종 상태값을 초기화
        glClearColor(0.8, 0.8, 0.6, 1.0)
    
    def resizeGL(sef, width, height) :
        # 카메라의 투영 특성을 여기서 설정
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

    def paintGL(self) :
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        glColor(0, -1, 1)

        ix, iy, iz = -1, 0, 0
        fx, fy, fz = 1.0, 0.0, 0.0
        fverts = [fx -1.0, fy + 1.0, fz]

        glBegin(GL_TRIANGLES)
        glVertex3i(ix, iy, iz)
        glVertex3f(fx, fy, fz)
        glVertex3fv(fverts)
        glEnd()

        #그려진 프레임버퍼를 화면에 송출
        glFlush()

def main(argv = []) :
    app = QApplication(argv)
    window = MyGLWindow()
    window.setWindowTitle("Primitive")
    window.setFixedSize(600, 600)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__" :
    main(sys.argv)
