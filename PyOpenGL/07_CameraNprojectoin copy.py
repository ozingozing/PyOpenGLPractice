from OpenGL.GL import *
from OpenGL.GLU import *

from PyQt6.QtWidgets import *
from PyQt6.QtOpenGLWidgets import *

import sys


class MyGLWindow(QOpenGLWidget) :
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("glOrtho")

    def initializeGL(self) :
        glClearColor(0.1, 0.7, 0.3, 1.0)

    def resizeGL(self, w: int, h: int) :
        aspRatio = w / h
        range = 2
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-range * aspRatio, range * aspRatio, -range , range, -range, range)


    def paintGL(self) :
        glClear(GL_COLOR_BUFFER_BIT |  GL_DEPTH_BUFFER_BIT)

        glBegin(GL_POLYGON)
        glColor3f(1, 1, 0)
        glVertex3f(1, 0, 0)
        glVertex3f(0, 1, 0)
        glVertex3f(-1, 0, 0)
        glVertex3f( 0, -1, 0)
        glEnd()

def main(argv = sys.argv) :
    app = QApplication(argv)
    window = MyGLWindow()
    window.show()

    app.exec()

if __name__ == "__main__" :
    main(sys.argv)