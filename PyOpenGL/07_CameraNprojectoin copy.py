from OpenGL.GL import *
from OpenGL.GLU import *

from PyQt6.QtWidgets import *
from PyQt6.QtOpenGLWidgets import *
import sys
def DrawAxes() :
    glBegin(GL_LINES)
    glColor(1, 0, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(1, 0 ,0)

    glColor(0, 1, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 1 ,0)

    glColor(0, 0, 1)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0 ,1)
    glEnd()

class MyGLWindow(QOpenGLWidget) : #QOpenGLWidget 상속
    def __init__(self) :
        super().__init__()  #QMainWindow 생성자 실행
        self.setWindowTitle("glOrtho 연습!")

    def initializeGL(self) :
        glClearColor(0.1, 0.7, 0.3, 1.0)

    def resizeGL(self, w: int, h: int) :
        aspR = w/h
        range = 1
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        
        glOrtho(-range*aspR, range*aspR, 
                -range, range, -range, range)
    
    def paintGL(slef) :
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glBegin(GL_POLYGON)
        glColor3f(1, 1, 0)
        glVertex3f(1, 0, 0)
        glVertex3f(0, 1, 0)
        glVertex3f(-1, 0, 0)
        glVertex3f( 0, -1, 0)
        glEnd()
        DrawAxes()

def main(argv = sys.argv) :
    app = QApplication(argv)
    window = MyGLWindow()
    window.show()
    app.exec()

if __name__ == "__main__" :
    main(sys.argv)
