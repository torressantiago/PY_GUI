import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class mainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.InitGUI()

    def InitGUI(self):
        self.setWindowTitle('Hello')
        self.resize(480,320)
        # use a grid arrangement style and create listeners for buttons
        self.layout=QGridLayout() 
        self.button1=QPushButton('1',None)
        self.button1.clicked.connect(self.button)

        self.button2=QPushButton('2',None)
        self.button2.clicked.connect(self.button)

        self.button3=QPushButton('3',None)
        self.button3.clicked.connect(self.button)

        # An image can also be added as a button
        self.image=QPixmap('Widgets/Announce.png')
        self.labelimage = QLabel() # Attach image to elder window
        self.labelimage.setPixmap(self.image)
        # The rest is pretty similar to the pushbutton
        self.layout.addWidget(self.labelimage, 0, 0, 4, 4)

        # Set the coordinated for the button in the grid
        self.layout.addWidget(self.button1, 0, 0, 1, 2) # A button can be defined over multiple cells
        self.layout.addWidget(self.button2, 0, 3) # Or a single cell

        # A button can also be configured through CSS styling
        self.button3.setStyleSheet("background-color: #FF00FF; border-radius: 5px; border: 2px solid gray;")
        self.layout.addWidget(self.button3, 3, 4)

        self.setLayout(self.layout)
        self.show()
    
    # Listener callback for buttons
    def button(self):
        sender = self.sender()
        print(f'Button {sender.text()} pushed')

if __name__=='__main__':
    app = QApplication(sys.argv)
    HMI = mainWindow()
    app.exec_()