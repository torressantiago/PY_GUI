from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from thermo import thermo

from matplotlib import pyplot as plot
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import random
import numpy as np

import sys

class Monitoring(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.status = 0
        self.course = 0
        # variables serving the aggregate simulation curve
        self.tabval = []
        self.Index = 0
        self.InitGUI()

    def InitGUI(self):
        self.base = QWidget()
        self.base.setWindowTitle("Weather station")
        self.resize(1280,720)

        # tab creation
        self.tab = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab.addTab(self.tab1, "Information")
        self.tab.addTab(self.tab2, "History")

        self.mainlayout = QGridLayout()
        self.mainlayout.addWidget(self.tab)

        self.bt1 = QPushButton("OK")
        self.Pstatus = QProgressBar()
        self.Hstatus = QProgressBar()
        self.RSSIstatus = QProgressBar()
        self.thermo = thermo()
        self.Plabel = QLabel('Pressure')
        self.Hlabel = QLabel('Humidity')
        self.RSSIlabel = QLabel('RSSI')
        self.infolayout = QGridLayout()
        self.infolayout.addWidget(self.Plabel,0,0)
        self.infolayout.addWidget(self.Hlabel,1,0)
        self.infolayout.addWidget(self.RSSIlabel,2,0)
        self.infolayout.addWidget(self.Pstatus,0,1)
        self.infolayout.addWidget(self.Hstatus,1,1)
        self.infolayout.addWidget(self.RSSIstatus,2,1)
        self.infolayout.setHorizontalSpacing(40)
        self.infolayout.addWidget(self.thermo, 0,3,3,1)
        self.infolayout.addWidget(self.bt1,3,3)
        self.tab1.setLayout(self.infolayout)

        self.dyn_canv = FigureCanvas(Figure(figsize = (5,5)))
        self.ax_dyn = self.dyn_canv.figure.subplots()

        self.timer = self.dyn_canv.new_timer(interval = 100)
        self.timer.add_callback(self.trace, self.ax_dyn)
        self.timer.start()

        self.courbelayout = QGridLayout()
        self.courbelayout.addWidget(self.dyn_canv)
        self.tab2.setLayout(self.courbelayout)
    
    def trace(self, ax):
        ax.figure.canvas.draw()
        self.Index += 1
        self.val = random.random()
        self.tabval.append(self.val)
        ax.plot(np.asarray(self.tabval))

        self.base.setLayout(self.mainlayout)
        self.base.show()

    def setPval(self, val):
        self.Pstatus.setValue(val)
    
    def setHval(self, val):
        self.Hstatus.setValue(val)

    def setRSSI(self, val):
        self.RSSIstatus.setValue(val)

    def setTemp(self, val):
        self.thermo.setTemp(val)

    def getTemp():
        tt = psutil.sensors_temperatures()
        temp_list = []
        for n,i in tt.items():
            for ii in i:
                temp_list.append(ii.current)
        return temp_list

    def show():
        IHM.setPval(int(psutil.cpu_percent(0.5)))
        IHM.setHval(int(psutil.virtual_memory().percent))
        IHM.setRSSI(int(psutil.sensors_battery().percent))
        temp=get_temp()
        IHM.setTemp(int(temp[0])) # Average CPU temp

if __name__=='__main__':
    app = QApplication(sys.argv)
    HMI = Monitoring()
    app.exec_()