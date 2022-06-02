from PyQt5 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
from random import randint

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        self.x1 = list(range(1))  # 100 time points
        self.y1 = [randint(0,1500) for _ in range(1)]  # 100 data points

        self.y2 = [randint(0,1500) for _ in range(1)]  # 100 data points
        self.y3 = [randint(0,1500) for _ in range(1)]  # 100 data points
        self.y4 = [randint(0,1500) for _ in range(1)]  # 100 data points

        self.graphWidget.setBackground('w')

        pen = pg.mkPen(color=(255, 0, 0))
        self.x1 = self.x1[1:]  # Remove the first y1 element.
        self.y1 = self.y1[1:]  # Remove the first
        self.y2 = self.y2[1:]  # Remove the first
        self.y3 = self.y3[1:]  # Remove the first
        self.y4 = self.y4[1:]  # Remove the first

        self.data_line =  self.graphWidget.plot(self.x1, self.y1, pen=pen)
        self.data_line2 =  self.graphWidget.plot(self.x1, self.y2, pen=("g"))
        self.data_line3 =  self.graphWidget.plot(self.x1, self.y3, pen=("b"))
        self.data_line4 =  self.graphWidget.plot(self.x1, self.y4, pen=("y"))

        self.timer = QtCore.QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()
        self.second = 0

    def update_plot_data(self):
        #self.x1 = self.x1[1:]  # Remove the first y element.
        if len(self.x1)>60:
            self.x1 = self.x1[1:]  # Add a new value 1 higher than the last.
            self.y1 = self.y1[1:]  # Remove the first
            self.y2 = self.y2[1:]  # Remove the first
            self.y3 = self.y3[1:]  # Remove the first
            self.y4 = self.y4[1:]  # Remove the first
        self.x1.append(self.second)
        self.second = self.second + 1
        self.y1.append(randint(0,1500))  # Add a new random value.
        self.y2.append(randint(0,1500))  # Add a new random value.
        self.y3.append(randint(0,1500))  # Add a new random value.
        self.y4.append(randint(0,1500))  # Add a new random value.

        self.data_line.setData(self.x1, self.y1)  # Update the data.
        self.data_line2.setData(self.x1, self.y2)  # Update the data
        self.data_line3.setData(self.x1, self.y3)  # Update the data
        self.data_line4.setData(self.x1, self.y4)  # Update the data

app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())
