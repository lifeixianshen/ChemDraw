from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QWidget
from PyQt5 import uic,QtCore,QtWidgets,QtGui
from mydesign import Ui_ChemDraw  # to genrate this file run this in cmd--> pyuic5 E:/PFD/PFDui.ui -o E:/PFD/mydesign.py
import sys
import time
global UO
global icon
global icon_select

icon_select = 0

class mywindow(QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_ChemDraw()
        self.ui.setupUi(self)
        self.show()

        #Signal generator
        self.ui.pushButton_heater.clicked.connect(self.heater_main)
        self.ui.pushButton_cooler.clicked.connect(self.cooler_main)
        self.scene = QtWidgets.QGraphicsScene()
        self.ui.pfdenv.setScene(self.scene)
        self.ui.pfdenv.mousePressEvent = self.pfd_mousepress
        self.ui.pfdenv.mouseMoveEvent = self.pfd_mousemove

    #defination for graphics view
    def pfd_mousepress(self,e):
        x = e.x()
        y = e.y()
        global UO
        global icon_select
        if icon_select == 1:
            self.ui.log_pan.append("["+str(time.strftime("%H:%M:%S",time.localtime()))+"] "+str(UO)+" are dropped")
            icon_select = 0
        else:
            self.ui.log_pan.append("["+str(time.strftime("%H:%M:%S",time.localtime()))+"] "+"Please Select any Unit Operation")

    def pfd_mousemove(self,e):
        x = e.x()
        y = e.y()
        self.ui.status_lable.setText(str("x:")+str(x)+"  "+"y:"+str(y))

    # defination for icon menu
    def heater_main(self):
        self.ui.log_pan.append("["+str(time.strftime("%H:%M:%S",time.localtime()))+"] "+"Heater is ready to drop")
        global UO
        global icon_select
        UO = "Heater"
        icon_select = 1

    def cooler_main(self):
        self.ui.log_pan.append("["+str(time.strftime("%H:%M:%S",time.localtime()))+"] "+"Cooler is ready to drop")
        global UO
        global icon_select
        UO = "Cooler"
        icon_select = 1

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = mywindow()
    w.show()
    sys.exit(app.exec_())
