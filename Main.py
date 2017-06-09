import sys
import math

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets



class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.move(100, 100)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.setWindowTitle('Pimp my CUBE')
        self.setFixedSize(660, 210)


        self.Xangle = QtWidgets.QLineEdit(self)
        self.Xangle.setPlaceholderText("Angle for X")
        self.Xangle.move(100, 20)
        self.Xangle.resize(100, 30)

        self.Yangle = QtWidgets.QLineEdit(self)
        self.Yangle.setPlaceholderText("Angle for Y")
        self.Yangle.move(250, 20)
        self.Yangle.resize(100, 30)

        self.Zangle = QtWidgets.QLineEdit(self)
        self.Zangle.setPlaceholderText("Angle for Z")
        self.Zangle.move(400, 20)
        self.Zangle.resize(100, 30)

        self.Before = QtWidgets.QTextEdit(self)
        self.Before.move(20, 60)
        self.Before.resize(300, 130)
        self.Before.setFont(QtGui.QFont("Courier", 9))

        self.After = QtWidgets.QTextEdit(self)
        self.After.move(340, 60)
        self.After.resize(300, 130)
        self.After.setFont(QtGui.QFont("Courier", 9))

        self.Changebtn = QtWidgets.QPushButton('PIMP IT111!!', self)
        self.Changebtn.setGeometry(540, 20, 100, 30)
        self.Changebtn.clicked[bool].connect(self.TimeToPimp)
        self.show()
    def TimeToPimp(self):
        self.halfLength = 1
        self.angles = [int(self.Xangle.text()), int(self.Yangle.text()), int(self.Zangle.text())]
        self.vertices = \
        [
            [-self.halfLength, -self.halfLength, -self.halfLength],
            [-self.halfLength, -self.halfLength, self.halfLength],
            [-self.halfLength, self.halfLength, -self.halfLength],
            [-self.halfLength, self.halfLength, self.halfLength],
            [-self.halfLength, -self.halfLength, -self.halfLength],
            [self.halfLength, -self.halfLength, self.halfLength],
            [self.halfLength, self.halfLength, -self.halfLength],
            [self.halfLength, self.halfLength, self.halfLength],
        ]
        self.Before.setText(str(self.vertices))

        cos = round(math.cos(math.radians(self.angles[0])), 8)
        sin = round(math.sin(math.radians(self.angles[0])), 8)
        for num in range(8):
            vertex = self.vertices[num]
            self.vertices[num] = [vertex[0], (cos * vertex[1]) - (sin * vertex[2]), sin * vertex[1] + cos * vertex[2]]

        cos = round(math.cos(math.radians(self.angles[1])), 8)
        sin = round(math.sin(math.radians(self.angles[1])), 8)
        for num in range(8):
            vertex = self.vertices[num]
            self.vertices[num] = [cos * vertex[0] - sin * vertex[2], vertex[1], sin * vertex[0] + cos * vertex[2]]

        cos = round(math.cos(math.radians(self.angles[2])), 8)
        sin = round(math.sin(math.radians(self.angles[2])), 8)
        for num in range(8):
            vertex = self.vertices[num]
            self.vertices[num] = [cos * vertex[0] - sin * vertex[1], sin * vertex[0] + cos * vertex[1], vertex[2]]

        self.After.setText(str(self.vertices))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
sys.exit(app.exec_())