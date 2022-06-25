import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class thermo(QWidget):
    colorChanged=pyqtSignal(int)
    valueChanged=pyqtSignal(int)

    def __init__(self) -> None:
        super().__init__(parent)
        self.radius = 20
        self.height = 80
        self.width = self.radius
        self.color = Qt.green
        self.value = 25
        self.h = self.value
        self.max = 60
        self.min = -20
        self.cold = 0
        self.hot = 30
        self.initGui()
    
    def setTemp(self, val):
        self.value = val
        self.update()

    def initGui(self):
        self.setGeometry(0,0,4*self.radius+self.height)
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)

        pen = QPen()
        pen.setWidth(1)
        pen.setColor(Qt.white)
        qp.setPen(pen)
        qp.setBrush(Qt.white)
        qp.drawRect(int(self.radius/2), 5, self.width, self.height + self.radius)

        if self.value < self.cold:
            pen.setColor(Qt.blue)
            qp.setPen(pen)
            qp.setBrush(Qt.blue)
        elif self.value > self.hot:
            pen.setColor(Qt.red)
            qp.setPen(pen)
            qp.setBrush(Qt.red)
        else:
            pen.setColor(Qt.green)
            qp.setPen(pen)
            qp.setBrush(Qt.green)

            qp.drawEllipse(0, self.height+20, 2*self.radius, 2*self.radius)
            qp.drawRect(int(self.radius/2),self.height+20+5,self.width, -(5+self.radius)-self.value)

            # Show thermometer temperature
            pen.setColor(Qt.black)
            qp.setPen(pen)
            qp.setFont(QFont('Arial', 12))
            qp.drawText(int(self.radius/2),(self.height+2*self.radius+5),str(self.value))
            qp.end

    def changeColor(self, color):
        self.color = color
        self.colorChanged.emit(self.color)
        self.update()

    def changeValue(self, value):
        self.value = value
        self.valueChanged.emit(self.value)
        self.h = self.value + 20
        self.update()