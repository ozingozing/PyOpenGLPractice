from OpenGL.GL import *
from OpenGL.GLU import *

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtOpenGLWidgets import QOpenGLWidget
from PyQt6.QtCore import *

import sys
import numpy as np

class MeshLoader :
    def __init__(self) :
        self.nV = 0 #정점의 개수
        self.nF = 0 #면의 개수
        self.vBuffer = None #정점 버퍼
        self.iBuffer = None #면을 표현하는 인데스 버퍼

    def loadMesh(self, filename) :
        with open(filename, 'rt') as inputfile :
            #with 구문 내부블럭 시작
            self.nV = int(next(inputfile))
            self.vBuffer = np.zeros((self.nV * 3, ), dtype = float)
            for i in range(self.nV) :
                verts = next(inputfile).split()
                self.vBuffer[i * 3 : i * 3 + 3] = verts

            self.nF = int(next(inputfile))
            self.iBuffer = np.zeros((self.nF * 3, ), dtype = int)
            for i in range (self.nF) :
                idx = next(inputfile).split() # idx[0] : 면을 구성하는 점의 개수
                # 필요한 정보는 idx[1], idx[2], idx[3] = idx[1 : 4]
                self.iBuffer[i * 3 : i * 3 + 3] = idx[1 : 4]
            # with 구문의 내부 블럭 끝
    
    def draw(self) :
        glPointSize(5)

        glBegin(GL_TRIANGLES)
        for i in range (self.nF) :
            #각 면을 그린다.
            #각 면을 구성하는 정점의 번호는
            v = self.iBuffer[i * 3 : i * 3 + 3]
            #각 정점은 v[0], v[1], v[2]
            #첫 점은 v[0]의 번호를 가진 정점을 vBuffer에서 찾는다
            glColor3fv((self.vBuffer[v[0] * 3 : v[0] * 3 + 3] + np.array([1])) / 2.0)
            glVertex3fv(self.vBuffer[v[0] * 3 : v[0] * 3 + 3])
            
            #두 번째 점은 v[1]의 번호를 가진 정점을 vBuffer에서 찾는다
            glColor3fv((self.vBuffer[v[0] * 3 : v[0] * 3 + 3] + np.array([1])) / 2.0)
            glVertex3fv(self.vBuffer[v[1] * 3 : v[1] * 3 + 3])

            #세 번째 점은 v[2]의 번호를 가진 정점을 vBuffer에서 찾는다
            glColor3fv((self.vBuffer[v[0] * 3 : v[0] * 3 + 3] + np.array([1])) / 2.0)
            glVertex3fv(self.vBuffer[v[2] * 3 : v[2] * 3 + 3])
        glEnd()

        glColor3f(0, 0, 1)
        for i in range(self.nF) :
            glBegin(GL_LINE_LOOP)
            #각 면을 그린다.
            # 각 면을 구성하는 정점의 번호는
            v = self.iBuffer[i * 3 : i * 3 + 3]
            #각 정점은 v[0], v[1], v[2]
            #첫 점은 v[0]의 번호를 가진 정점을 vBuffer에서 찾는다
            glVertex3fv(self.vBuffer[v[0] * 3 : v[0] * 3 + 3])
            #두 번째 점은 v[1]의 번호를 가진 정점을 vBuffer에서 찾는다
            glVertex3fv(self.vBuffer[v[1] * 3 : v[1] * 3 + 3])
            #세 번째 점은 v[2]의 번호를 가진 정점을 vBuffer에서 찾는다
            glVertex3fv(self.vBuffer[v[2] * 3 : v[2] * 3 + 3])
            glEnd()    


class MyGLWidget(QOpenGLWidget) :
    def __init__(self, parent = None) :
        super().__init__(parent)

    def initializeGL(self) :
        #OpenGL 그리기를 수행하기 전에 각종 상태값을 초기화
        glClearColor(0.0, 0.0, 0.0, 1.0)
        self.myLoader = MeshLoader()
        self.myLoader.loadMesh(".\PyOpenGLPractice\TxtFile\cow.txt")
        self.angle = 0
        #ㅈㄴ 빨리 그리기 -> DisplayList 사용법
        self.drawFastList = glGenLists(1) #리스트 호출해
        glNewList(self.drawFastList, GL_COMPILE) #설정해
        self.myLoader.draw() #페인트 함수에 그릴놈 미리 불러!
        glEndList() #리스트 닫아!

    def resizeGL(self, width, height) :
        #카메라의 투영 특성을 여기서 설정
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60, width/height, 0.1, 100)

    def paintGL(self) :
        glClear(GL_COLOR_BUFFER_BIT)
        #특정 좌표 (0,0,0)에 도형을 그린다면 GL_MODELVIEW  매트릭스를 곱해서 실제적인 위치 지정.
        #GL_MODELVIEW 의 매트릭스가 변경이 되어 있다면은 전혀 다른 죄표에 그려지게 되어 있음.
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        """
        - eyeX, eyeY, eyeZ : 눈의 위치(카메라의 위치)
        - centerX, centerY, centerZ : 카메라의 초점(참조 위치)
        - upX, upY, upZ : 카메라의 위쪽벡터 방향 지정
        ^^(x가 1이면 x축으로 누워있고, y가 1이면 y축을 중심으로 세워져있다.)
        """
        gluLookAt(0,2,6, 0,0,0, 0,1,0)

        glRotatef(self.angle, 0, 1, 0)
        glCallList(self.drawFastList) #initialize에 설정했던 리스트 호출해!
        self.angle += 1.0

class MyWindow(QMainWindow):

    def __init__(self, title=''):
        QMainWindow.__init__(self)  # QMainWindow 슈퍼 클래스의 초기화
        self.setWindowTitle(title)

        self.glWidget = MyGLWidget()  # OpenGL Widget
        self.setCentralWidget(self.glWidget)

        self.timer = QTimer(self)
        self.timer.setInterval(1)
        self.timer.timeout.connect(self.timeout)
        self.timer.start()
    
    def timeout(self) :
        self.glWidget.update()

def main(argv = []):
    app = QApplication(argv)
    window = MyWindow('glDrawElements')
    window.setFixedSize(600, 600)
    window.show()
    app.exec()

if __name__ == "__main__" :
    main(sys.argv)