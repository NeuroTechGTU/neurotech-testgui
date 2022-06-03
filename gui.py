from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import *
import sys

 
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.acceptDrops()
        # set the title
        self.setWindowTitle("NeuroTech Test Application")
     #   self.setWindowIcon(QtGui.QIcon('imgsrc/logo.png'))
        # setting  the geometry of window
        self.setGeometry(0, 0, 1280, 720)
        self.setFixedSize(self.size())
        # creating label
        self.logo = QLabel(self)
        self.showMaximized()
        # loading image
        self.logo_pixmap = QPixmap('imgsrc/logo.png')
        self.logo_pixmap.scaled(50,50)
        self.logo_pixmap.scaled(32, 32)
        # adding image to label
        self.logo.setPixmap(self.logo_pixmap)
        a = self.logo_pixmap.width
        b = self.logo_pixmap.height
        # Optional, resize label to image size
        self.logo.resize(150,150)
        self.logo.move(500, 0)

        self.name = QLabel(self)
        self.name.setText("NEUROTECH")
        self.name.move(550,175)
 
        # show all the widgets
        self.show()
 
# create pyqt5 app
App = QApplication(sys.argv)
 
# create the instance of our Window
window = Window()
 
# start the app
sys.exit(App.exec())