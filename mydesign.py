# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:/PFD/PFDui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChemDraw(object):
    def setupUi(self, ChemDraw):
        ChemDraw.setObjectName("ChemDraw")
        ChemDraw.resize(1120, 834)
        ChemDraw.setMouseTracking(False)
        ChemDraw.setTabletTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ChemDraw.setWindowIcon(icon)
        ChemDraw.setIconSize(QtCore.QSize(24, 24))
        self.centralwidget = QtWidgets.QWidget(ChemDraw)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pfdenv = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pfdenv.sizePolicy().hasHeightForWidth())
        self.pfdenv.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pfdenv.setFont(font)
        self.pfdenv.setMouseTracking(True)
        self.pfdenv.setTabletTracking(True)
        self.pfdenv.setAcceptDrops(True)
        self.pfdenv.setAutoFillBackground(True)
        self.pfdenv.setStyleSheet("")
        self.pfdenv.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.pfdenv.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 127))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.pfdenv.setBackgroundBrush(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.pfdenv.setForegroundBrush(brush)
        self.pfdenv.setSceneRect(QtCore.QRectF(0.0, 0.0, 5000.0, 5000.0))
        self.pfdenv.setDragMode(QtWidgets.QGraphicsView.RubberBandDrag)
        self.pfdenv.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.pfdenv.setResizeAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.pfdenv.setViewportUpdateMode(QtWidgets.QGraphicsView.FullViewportUpdate)
        self.pfdenv.setOptimizationFlags(QtWidgets.QGraphicsView.DontClipPainter)
        self.pfdenv.setObjectName("pfdenv")
        self.verticalLayout_3.addWidget(self.pfdenv)
        self.Icon_window = QtWidgets.QDockWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Icon_window.sizePolicy().hasHeightForWidth())
        self.Icon_window.setSizePolicy(sizePolicy)
        self.Icon_window.setMinimumSize(QtCore.QSize(343, 200))
        self.Icon_window.setMaximumSize(QtCore.QSize(524287, 200))
        self.Icon_window.setAllowedAreas(QtCore.Qt.BottomDockWidgetArea)
        self.Icon_window.setObjectName("Icon_window")
        self.icon = QtWidgets.QWidget()
        self.icon.setObjectName("icon")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.icon)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.icon_tab = QtWidgets.QTabWidget(self.icon)
        self.icon_tab.setObjectName("icon_tab")
        self.tab_pipe = QtWidgets.QWidget()
        self.tab_pipe.setObjectName("tab_pipe")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_pipe)
        self.gridLayout.setObjectName("gridLayout")
        self.pipe_tab = QtWidgets.QTabWidget(self.tab_pipe)
        self.pipe_tab.setObjectName("pipe_tab")
        self.tab_straight = QtWidgets.QWidget()
        self.tab_straight.setObjectName("tab_straight")
        self.pipe_tab.addTab(self.tab_straight, "")
        self.tab_elbow = QtWidgets.QWidget()
        self.tab_elbow.setObjectName("tab_elbow")
        self.pipe_tab.addTab(self.tab_elbow, "")
        self.tab_valve = QtWidgets.QWidget()
        self.tab_valve.setObjectName("tab_valve")
        self.pipe_tab.addTab(self.tab_valve, "")
        self.gridLayout.addWidget(self.pipe_tab, 0, 0, 1, 1)
        self.icon_tab.addTab(self.tab_pipe, "")
        self.tab_heat = QtWidgets.QWidget()
        self.tab_heat.setObjectName("tab_heat")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_heat)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_heater = QtWidgets.QPushButton(self.tab_heat)
        self.pushButton_heater.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/Heater.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_heater.setIcon(icon1)
        self.pushButton_heater.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_heater.setFlat(True)
        self.pushButton_heater.setObjectName("pushButton_heater")
        self.gridLayout_3.addWidget(self.pushButton_heater, 1, 1, 1, 1)
        self.pushButton_cooler = QtWidgets.QPushButton(self.tab_heat)
        self.pushButton_cooler.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/Cooler.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_cooler.setIcon(icon2)
        self.pushButton_cooler.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_cooler.setShortcut("")
        self.pushButton_cooler.setFlat(True)
        self.pushButton_cooler.setObjectName("pushButton_cooler")
        self.gridLayout_3.addWidget(self.pushButton_cooler, 1, 2, 1, 1)
        self.label_heater = QtWidgets.QLabel(self.tab_heat)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_heater.setFont(font)
        self.label_heater.setAlignment(QtCore.Qt.AlignCenter)
        self.label_heater.setObjectName("label_heater")
        self.gridLayout_3.addWidget(self.label_heater, 4, 1, 1, 1)
        self.label_cooler = QtWidgets.QLabel(self.tab_heat)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_cooler.setFont(font)
        self.label_cooler.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cooler.setObjectName("label_cooler")
        self.gridLayout_3.addWidget(self.label_cooler, 4, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 3, 1, 1)
        self.icon_tab.addTab(self.tab_heat, "")
        self.tab_pressure = QtWidgets.QWidget()
        self.tab_pressure.setObjectName("tab_pressure")
        self.icon_tab.addTab(self.tab_pressure, "")
        self.tab_reactor = QtWidgets.QWidget()
        self.tab_reactor.setObjectName("tab_reactor")
        self.icon_tab.addTab(self.tab_reactor, "")
        self.tab_columns = QtWidgets.QWidget()
        self.tab_columns.setObjectName("tab_columns")
        self.icon_tab.addTab(self.tab_columns, "")
        self.tab_solid = QtWidgets.QWidget()
        self.tab_solid.setObjectName("tab_solid")
        self.icon_tab.addTab(self.tab_solid, "")
        self.tab_user = QtWidgets.QWidget()
        self.tab_user.setObjectName("tab_user")
        self.icon_tab.addTab(self.tab_user, "")
        self.gridLayout_2.addWidget(self.icon_tab, 0, 0, 1, 1)
        self.Icon_window.setWidget(self.icon)
        self.verticalLayout_3.addWidget(self.Icon_window)
        self.log_window = QtWidgets.QDockWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.log_window.sizePolicy().hasHeightForWidth())
        self.log_window.setSizePolicy(sizePolicy)
        self.log_window.setMinimumSize(QtCore.QSize(111, 150))
        self.log_window.setMaximumSize(QtCore.QSize(524287, 150))
        self.log_window.setAllowedAreas(QtCore.Qt.BottomDockWidgetArea)
        self.log_window.setObjectName("log_window")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.log_pan = QtWidgets.QTextEdit(self.dockWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(10)
        self.log_pan.setFont(font)
        self.log_pan.setAcceptDrops(False)
        self.log_pan.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.log_pan.setReadOnly(True)
        self.log_pan.setObjectName("log_pan")
        self.verticalLayout_2.addWidget(self.log_pan)
        self.log_window.setWidget(self.dockWidgetContents_2)
        self.verticalLayout_3.addWidget(self.log_window)
        self.status_lable = QtWidgets.QLabel(self.centralwidget)
        self.status_lable.setText("")
        self.status_lable.setObjectName("status_lable")
        self.verticalLayout_3.addWidget(self.status_lable)
        ChemDraw.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ChemDraw)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1120, 31))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuImport = QtWidgets.QMenu(self.menuFile)
        self.menuImport.setObjectName("menuImport")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        ChemDraw.setMenuBar(self.menubar)
        self.actionHelp = QtWidgets.QAction(ChemDraw)
        self.actionHelp.setObjectName("actionHelp")
        self.actionSave = QtWidgets.QAction(ChemDraw)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_2 = QtWidgets.QAction(ChemDraw)
        self.actionSave_2.setObjectName("actionSave_2")
        self.actionSave_As = QtWidgets.QAction(ChemDraw)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionImport_as_PDf = QtWidgets.QAction(ChemDraw)
        self.actionImport_as_PDf.setObjectName("actionImport_as_PDf")
        self.actionImport_as_jpg = QtWidgets.QAction(ChemDraw)
        self.actionImport_as_jpg.setObjectName("actionImport_as_jpg")
        self.actionImport_as_png = QtWidgets.QAction(ChemDraw)
        self.actionImport_as_png.setObjectName("actionImport_as_png")
        self.actionImport_as_scg = QtWidgets.QAction(ChemDraw)
        self.actionImport_as_scg.setObjectName("actionImport_as_scg")
        self.actionExit = QtWidgets.QAction(ChemDraw)
        self.actionExit.setObjectName("actionExit")
        self.actionDocumentation = QtWidgets.QAction(ChemDraw)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.actionHelp_us = QtWidgets.QAction(ChemDraw)
        self.actionHelp_us.setObjectName("actionHelp_us")
        self.actionAbout = QtWidgets.QAction(ChemDraw)
        self.actionAbout.setObjectName("actionAbout")
        self.menuImport.addAction(self.actionImport_as_PDf)
        self.menuImport.addAction(self.actionImport_as_jpg)
        self.menuImport.addAction(self.actionImport_as_png)
        self.menuImport.addAction(self.actionImport_as_scg)
        self.menuFile.addAction(self.actionSave_2)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.menuImport.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionDocumentation)
        self.menuHelp.addAction(self.actionHelp_us)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(ChemDraw)
        self.icon_tab.setCurrentIndex(1)
        self.pipe_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ChemDraw)

    def retranslateUi(self, ChemDraw):
        _translate = QtCore.QCoreApplication.translate
        ChemDraw.setWindowTitle(_translate("ChemDraw", "ChemDraw"))
        self.Icon_window.setWindowTitle(_translate("ChemDraw", "Icon"))
        self.pipe_tab.setTabText(self.pipe_tab.indexOf(self.tab_straight), _translate("ChemDraw", "Straight"))
        self.pipe_tab.setTabText(self.pipe_tab.indexOf(self.tab_elbow), _translate("ChemDraw", "Elbow"))
        self.pipe_tab.setTabText(self.pipe_tab.indexOf(self.tab_valve), _translate("ChemDraw", "Valve"))
        self.icon_tab.setTabText(self.icon_tab.indexOf(self.tab_pipe), _translate("ChemDraw", "Pipe"))
        self.label_heater.setText(_translate("ChemDraw", "Heater"))
        self.label_cooler.setText(_translate("ChemDraw", "Cooler"))
        self.icon_tab.setTabText(self.icon_tab.indexOf(self.tab_heat), _translate("ChemDraw", "Heat Exchanger"))
        self.icon_tab.setTabText(self.icon_tab.indexOf(self.tab_pressure), _translate("ChemDraw", "Pressure Chanager"))
        self.icon_tab.setTabText(self.icon_tab.indexOf(self.tab_reactor), _translate("ChemDraw", "Reactor"))
        self.icon_tab.setTabText(self.icon_tab.indexOf(self.tab_columns), _translate("ChemDraw", "Columns"))
        self.icon_tab.setTabText(self.icon_tab.indexOf(self.tab_solid), _translate("ChemDraw", "Solid"))
        self.icon_tab.setTabText(self.icon_tab.indexOf(self.tab_user), _translate("ChemDraw", "User Define"))
        self.log_window.setWindowTitle(_translate("ChemDraw", "Log"))
        self.log_pan.setPlaceholderText(_translate("ChemDraw", "Welcome to ChemDraw, an OpenSource P&ID devlopment tool"))
        self.menuFile.setTitle(_translate("ChemDraw", "File"))
        self.menuImport.setTitle(_translate("ChemDraw", "Import"))
        self.menuEdit.setTitle(_translate("ChemDraw", "Edit"))
        self.menuHelp.setTitle(_translate("ChemDraw", "Help"))
        self.actionHelp.setText(_translate("ChemDraw", "Help"))
        self.actionSave.setText(_translate("ChemDraw", "save"))
        self.actionSave_2.setText(_translate("ChemDraw", "Save"))
        self.actionSave_As.setText(_translate("ChemDraw", "Save As"))
        self.actionImport_as_PDf.setText(_translate("ChemDraw", "Import as PDf"))
        self.actionImport_as_jpg.setText(_translate("ChemDraw", "Import as jpg"))
        self.actionImport_as_png.setText(_translate("ChemDraw", "Import as png"))
        self.actionImport_as_scg.setText(_translate("ChemDraw", "Import as svg"))
        self.actionExit.setText(_translate("ChemDraw", "Exit"))
        self.actionDocumentation.setText(_translate("ChemDraw", "Documentation"))
        self.actionHelp_us.setText(_translate("ChemDraw", "Help us!"))
        self.actionAbout.setText(_translate("ChemDraw", "About"))