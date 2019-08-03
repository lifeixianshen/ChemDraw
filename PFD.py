from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QWidget
from PyQt5 import uic, QtCore, QtWidgets, QtGui
from mydesign import Ui_ChemDraw  # to generate this file run this in cmd--> pyuic5 E:/PFD/PFDui.ui -o E:/PFD/mydesign.py
import sys
import time

global UO
global icon
global icon_select

icon_select = 0
H_pos = 0
V_pos = 0


class mywindow(QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_ChemDraw()
        self.ui.setupUi(self)
        self.show()

        # Signal generator
        self.ui.pushButton_heater.clicked.connect(self.heater_main)
        self.ui.pushButton_cooler.clicked.connect(self.cooler_main)
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setItemIndexMethod(QtWidgets.QGraphicsScene.NoIndex)
        self.ui.pfdenv.setScene(self.scene)

        scroll_horizontal = self.ui.pfdenv.horizontalScrollBar()
        scroll_vertical = self.ui.pfdenv.verticalScrollBar()
        scroll_horizontal.valueChanged.connect(self.scroll_h)
        scroll_vertical.valueChanged.connect(self.scroll_v)

        # menubar
        self.ui.actionAbout.triggered.connect(self.About)
        self.ui.status_label_3.mousePressEvent = self.About_statusbar

    # defination for graphics view
    def scroll_v(self, V):
        global V_pos
        V_pos = V

    def scroll_h(self, H):
        global H_pos
        H_pos = H

    def addicon(self):
        if UO == "Heater":
            add_icon = self.scene.addPixmap(QtGui.QPixmap("icons\Heater.png"))
        if UO == "Cooler":
            add_icon = self.scene.addPixmap(QtGui.QPixmap("icons\Cooler.png"))
        add_icon.setPos(int(50 + H_pos), int(50 + V_pos))
        add_icon.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, True)
        add_icon.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, True)
        add_icon.setAcceptHoverEvents(True)
        add_icon.setAcceptTouchEvents(True)

    # definition for icon menu
    def heater_main(self):
        self.ui.log_pan.append(
            "[" + str(time.strftime("%H:%M:%S", time.localtime())) + "] " + "Heater is ready to drop")
        global UO
        global icon_select
        UO = "Heater"
        icon_select = 1
        self.addicon()

    def cooler_main(self):
        self.ui.log_pan.append(
            "[" + str(time.strftime("%H:%M:%S", time.localtime())) + "] " + "Cooler is ready to drop")
        global UO
        global icon_select
        UO = "Cooler"
        icon_select = 1
        self.addicon()

    # menubar action
    def About(self):
        msg = uic.loadUi("conf\About.ui")
        msg.show()
        msg.exec_()
    def About_statusbar(self,e):
        msg = uic.loadUi("conf\About.ui")
        msg.show()
        msg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = mywindow()
    w.show()
    sys.exit(app.exec_())
