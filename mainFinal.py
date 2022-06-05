from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtGui, QtWidgets,QtPrintSupport
from pyqtgraph import PlotWidget
import numpy as np
from PyQt5.QtWidgets import QFileDialog
from fpdf import FPDF
import os
class MatplotlibCanvas(FigureCanvasQTAgg):
	def __init__(self,parent=None, dpi = 120):
		fig = Figure(dpi = dpi)
		self.axes = fig.add_subplot(111)
		super(MatplotlibCanvas,self).__init__(fig)
		fig.tight_layout()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(946, 721)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_4_For_mainpulating = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_4_For_mainpulating.setTitle("")
        self.groupBox_4_For_mainpulating.setObjectName("groupBox_4_For_mainpulating")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_4_For_mainpulating)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.zoomI = QtWidgets.QPushButton(self.groupBox_4_For_mainpulating)
        self.zoomI.setObjectName("zoomI")
        self.gridLayout_8.addWidget(self.zoomI, 3, 2, 2, 1)
        self.scrollF = QtWidgets.QPushButton(self.groupBox_4_For_mainpulating)
        self.scrollF.setObjectName("scrollF")
        self.gridLayout_8.addWidget(self.scrollF, 3, 3, 2, 1)
        self.comboBox_For_selcting_color = QtWidgets.QComboBox(self.groupBox_4_For_mainpulating)
        self.comboBox_For_selcting_color.setObjectName("comboBox_For_selcting_color")
        self.comboBox_For_selcting_color.addItem("")
        self.comboBox_For_selcting_color.addItem("")
        self.comboBox_For_selcting_color.addItem("")
        self.comboBox_For_selcting_color.addItem("")
        self.gridLayout_8.addWidget(self.comboBox_For_selcting_color, 6, 0, 1, 1)
        self.scrollB = QtWidgets.QPushButton(self.groupBox_4_For_mainpulating)
        self.scrollB.setObjectName("scrollB")
        self.gridLayout_8.addWidget(self.scrollB, 6, 3, 1, 1)
        self.savePDF = QtWidgets.QPushButton(self.groupBox_4_For_mainpulating)
        self.savePDF.setObjectName("savePDF")
        self.gridLayout_8.addWidget(self.savePDF, 6, 4, 1, 1)
        self.label_For_signal_viewr = QtWidgets.QLabel(self.groupBox_4_For_mainpulating)
        self.label_For_signal_viewr.setAlignment(QtCore.Qt.AlignCenter)
        self.label_For_signal_viewr.setObjectName("label_For_signal_viewr")
        self.gridLayout_8.addWidget(self.label_For_signal_viewr, 1, 0, 3, 1)
        self.open = QtWidgets.QPushButton(self.groupBox_4_For_mainpulating)
        self.open.setObjectName("open")
        self.gridLayout_8.addWidget(self.open, 4, 0, 1, 1)
        self.stop = QtWidgets.QPushButton(self.groupBox_4_For_mainpulating)
        self.stop.setObjectName("stop")
        self.gridLayout_8.addWidget(self.stop, 2, 3, 1, 1)
        self.play = QtWidgets.QPushButton(self.groupBox_4_For_mainpulating)
        self.play.setObjectName("play")
        self.gridLayout_8.addWidget(self.play, 2, 2, 1, 1)
        self.zoomO = QtWidgets.QPushButton(self.groupBox_4_For_mainpulating)
        self.zoomO.setObjectName("zoomO")
        self.gridLayout_8.addWidget(self.zoomO, 6, 2, 1, 1)
        self.PushButton_Speed_down = QtWidgets.QPushButton(self.groupBox_4_For_mainpulating)
        self.PushButton_Speed_down.setObjectName("PushButton_Speed_down")
        self.gridLayout_8.addWidget(self.PushButton_Speed_down, 4, 4, 1, 1)
        self.PushButton_Speed_up = QtWidgets.QPushButton(self.groupBox_4_For_mainpulating)
        self.PushButton_Speed_up.setObjectName("PushButton_Speed_up")
        self.gridLayout_8.addWidget(self.PushButton_Speed_up, 2, 4, 1, 1)
        self.verticalLayout_5.addWidget(self.groupBox_4_For_mainpulating)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = PlotWidget(self.layoutWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.label_for_control_speed = QtWidgets.QLabel(self.layoutWidget)
        self.label_for_control_speed.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_for_control_speed.setObjectName("label_for_control_speed")
        self.verticalLayout.addWidget(self.label_for_control_speed)
        self.horizontalSlider_for_controlling_speed = QtWidgets.QSlider(self.layoutWidget)
        self.horizontalSlider_for_controlling_speed.setMinimum(1)
        self.horizontalSlider_for_controlling_speed.setMaximum(5)
        self.horizontalSlider_for_controlling_speed.setPageStep(1)
        self.horizontalSlider_for_controlling_speed.setSliderPosition(3)
        self.horizontalSlider_for_controlling_speed.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_for_controlling_speed.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_for_controlling_speed.setTickInterval(1)
        self.horizontalSlider_for_controlling_speed.setObjectName("horizontalSlider_for_controlling_speed")
        self.verticalLayout.addWidget(self.horizontalSlider_for_controlling_speed)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_for_spectroGram = QtWidgets.QLabel(self.layoutWidget1)
        self.label_for_spectroGram.setAlignment(QtCore.Qt.AlignCenter)
        self.label_for_spectroGram.setObjectName("label_for_spectroGram")
        self.verticalLayout_4.addWidget(self.label_for_spectroGram)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.Spare_button = QtWidgets.QPushButton(self.layoutWidget1)
        self.Spare_button.setObjectName("Spare_button")
        self.horizontalLayout.addWidget(self.Spare_button)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.frame = QtWidgets.QFrame(self.layoutWidget1)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.verticalLayout_6)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.frame)
        self.horizontalSlider_2.setMaximum(10)
        self.horizontalSlider_2.setPageStep(1)
        self.horizontalSlider_2.setSliderPosition(5)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalLayout_3.addWidget(self.horizontalSlider_2)
        self.horizontalSlider = QtWidgets.QSlider(self.frame)
        self.horizontalSlider.setMaximum(10)
        self.horizontalSlider.setPageStep(1)
        self.horizontalSlider.setProperty("value", 5)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_3.addWidget(self.horizontalSlider)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addWidget(self.frame)
        self.horizontalLayout_for_check_boxes = QtWidgets.QHBoxLayout()
        self.horizontalLayout_for_check_boxes.setObjectName("horizontalLayout_for_check_boxes")
        self.Channel_1_Check_Box = QtWidgets.QCheckBox(self.layoutWidget1)
        self.Channel_1_Check_Box.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Channel_1_Check_Box.sizePolicy().hasHeightForWidth())
        self.Channel_1_Check_Box.setSizePolicy(sizePolicy)
        self.Channel_1_Check_Box.setMinimumSize(QtCore.QSize(5, 5))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.Channel_1_Check_Box.setFont(font)
        self.Channel_1_Check_Box.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Channel_1_Check_Box.setAutoFillBackground(False)
        self.Channel_1_Check_Box.setIconSize(QtCore.QSize(20, 20))
        self.Channel_1_Check_Box.setChecked(True)
        self.Channel_1_Check_Box.setTristate(False)
        self.Channel_1_Check_Box.setObjectName("Channel_1_Check_Box")
        self.horizontalLayout_for_check_boxes.addWidget(self.Channel_1_Check_Box)
        self.Channel_2_Check_Box = QtWidgets.QCheckBox(self.layoutWidget1)
        self.Channel_2_Check_Box.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Channel_2_Check_Box.sizePolicy().hasHeightForWidth())
        self.Channel_2_Check_Box.setSizePolicy(sizePolicy)
        self.Channel_2_Check_Box.setMinimumSize(QtCore.QSize(5, 5))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Channel_2_Check_Box.setFont(font)
        self.Channel_2_Check_Box.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Channel_2_Check_Box.setAutoFillBackground(False)
        self.Channel_2_Check_Box.setIconSize(QtCore.QSize(20, 20))
        self.Channel_2_Check_Box.setChecked(True)
        self.Channel_2_Check_Box.setTristate(False)
        self.Channel_2_Check_Box.setObjectName("Channel_2_Check_Box")
        self.horizontalLayout_for_check_boxes.addWidget(self.Channel_2_Check_Box)
        self.Channel_3_Check_Box = QtWidgets.QCheckBox(self.layoutWidget1)
        self.Channel_3_Check_Box.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Channel_3_Check_Box.sizePolicy().hasHeightForWidth())
        self.Channel_3_Check_Box.setSizePolicy(sizePolicy)
        self.Channel_3_Check_Box.setMinimumSize(QtCore.QSize(5, 5))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Channel_3_Check_Box.setFont(font)
        self.Channel_3_Check_Box.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Channel_3_Check_Box.setAutoFillBackground(False)
        self.Channel_3_Check_Box.setIconSize(QtCore.QSize(20, 20))
        self.Channel_3_Check_Box.setChecked(True)
        self.Channel_3_Check_Box.setTristate(False)
        self.Channel_3_Check_Box.setObjectName("Channel_3_Check_Box")
        self.horizontalLayout_for_check_boxes.addWidget(self.Channel_3_Check_Box)
        self.verticalLayout_4.addLayout(self.horizontalLayout_for_check_boxes)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.comboBox_For_selecting_Channel = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox_For_selecting_Channel.setObjectName("comboBox_For_selecting_Channel")
        self.comboBox_For_selecting_Channel.addItem("")
        self.comboBox_For_selecting_Channel.addItem("")
        self.comboBox_For_selecting_Channel.addItem("")
        self.verticalLayout_4.addWidget(self.comboBox_For_selecting_Channel)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem2)
        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem3, 0, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 1, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 946, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave_as_pdf = QtWidgets.QAction(MainWindow)
        self.actionSave_as_pdf.setObjectName("actionSave_as_pdf")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionSave_as_pdf)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.horizontalSlider_for_controlling_speed.valueChanged['int'].connect(self.PushButton_Speed_up.update)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Channel_1_Check_Box.stateChanged.connect(lambda: self.IsChecked())
        self.Channel_2_Check_Box.stateChanged.connect(lambda: self.IsChecked())
        self.Channel_3_Check_Box.stateChanged.connect(lambda: self.IsChecked())

        self.comboBox_For_selcting_color.addItem
        self.scrollF.clicked.connect(self.forward)
        self.scrollB.clicked.connect(self.backward)

        self.open.clicked.connect(self.getFile)
        self.stop.clicked.connect(self.stp)
        self.zoomI.clicked.connect(self.zoomin)
        self.zoomO.clicked.connect(self.zoomout)
        self.play.clicked.connect(self.playfn)

        self.PushButton_Speed_up.clicked.connect(self.faster)
        self.PushButton_Speed_down.clicked.connect(self.slower)
        self.savePDF.clicked.connect(self.ExportPDF)
        self.Spare_button.clicked.connect(self.spec)
        self.pushButton_2.clicked.connect(self.getLabel)

        self.filename = ''
        self.canvas = MatplotlibCanvas(self)
        self.plt = self.canvas.axes

        self.i1 = 0
        self.n1 = 0
        self.i2 = 0
        self.n2 = 0
        self.i3 = 0
        self.n3 = 0

        self.x1=[]
        self.y1=[]
        self.x2 = []
        self.y2 = []
        self.x3 = []
        self.y3 = []

        self.color = 0

        self.st = 0
        self.zm = 0
        self.f = 0

        self.name1=''
        self.name2=''
        self.name3=''

    def stp(self):
        self.st = 1

    def zoomin(self):
        self.zm = 1

    def zoomout(self):
        self.zm = 0

    def playfn(self):
        self.st = 0
        self.readdatatxt()

    def getLabel(self):
        if self.comboBox_For_selecting_Channel.currentIndex() == 0:
            label=self.lineEdit.text()
            self.name1=label
        elif self.comboBox_For_selecting_Channel.currentIndex() == 1:
            label = self.lineEdit.text()
            self.name2 = label
        elif self.comboBox_For_selecting_Channel.currentIndex() == 2:
            label = self.lineEdit.text()
            self.name3 = label

    def changeColorfn(self):
        if self.color == 0:
            self.graphicsView.setBackground(background=None)
            self.color = 1
        elif self.color == 1:
            self.graphicsView.setBackground(background='default')
            self.color = 0

    def forward(self):
        self.st = 1
        if self.comboBox_For_selecting_Channel.currentIndex()==0:
            self.graphicsView.clear()
            self.n1 += 50
            self.i1 += 25
            self.graphicsView.plot(self.x1[self.i1:self.n1], self.y1[self.i1:self.n1] , pen =[255,0,0], name = self.name1 )
            QtCore.QCoreApplication.processEvents()
        elif self.comboBox_For_selecting_Channel.currentIndex()==1:
            self.graphicsView.clear()
            self.n2 += 50
            self.i2 += 25
            self.n1 += 50
            self.i1 += 25
            self.graphicsView.plot(self.x1[self.i1:self.n1], self.y1[self.i1:self.n1], pen =[255,0,0], name = self.name1  )
            self.graphicsView.plot(self.x2[self.i2:self.n2], self.y2[self.i2:self.n2] , pen =[0,255,0], name=self.name2)
            QtCore.QCoreApplication.processEvents()
        elif self.comboBox_For_selecting_Channel.currentIndex()==2:
            self.graphicsView.clear()
            self.n3 += 50
            self.i3 += 25
            self.n2 += 50
            self.i2 += 25
            self.n1 += 50
            self.i1 += 25
            self.graphicsView.plot(self.x1[self.i1:self.n1], self.y1[self.i1:self.n1], pen =[255,0,0], name = self.name1  )
            self.graphicsView.plot(self.x2[self.i2:self.n2], self.y2[self.i2:self.n2] , pen =[0,255,0], name=self.name2)
            self.graphicsView.plot(self.x3[self.i3:self.n3], self.y3[self.i3:self.n3], pen =[0,0,255], name=self.name3 )
            QtCore.QCoreApplication.processEvents()

    def backward(self):
        self.st = 1
        if self.i1<=18:
            print("Max-Backward")
        else:
            if self.comboBox_For_selecting_Channel.currentIndex() == 0:
                self.graphicsView.clear()
                self.n1 -= 50
                self.i1 -= 25
                self.graphicsView.plot(self.x1[self.i1:self.n1], self.y1[self.i1:self.n1] , pen =[255,0,0], name = self.name1 )
                QtCore.QCoreApplication.processEvents()
            elif self.comboBox_For_selecting_Channel.currentIndex() == 1:
                self.graphicsView.clear()
                self.n2 -= 50
                self.i2 -= 25
                self.n1 -= 50
                self.i1 -= 25
                self.graphicsView.plot(self.x1[self.i1:self.n1], self.y1[self.i1:self.n1] , pen =[255,0,0], name = self.name1 )
                self.graphicsView.plot(self.x2[self.i2:self.n2], self.y2[self.i2:self.n2], pen =[0,255,0], name=self.name2 )
                QtCore.QCoreApplication.processEvents()
            elif self.comboBox_For_selecting_Channel.currentIndex() == 2:
                self.graphicsView.clear()
                self.n3 -= 50
                self.i3 -= 25
                self.n2 -= 50
                self.i2 -= 25
                self.n1 -= 50
                self.i1 -= 25
                self.graphicsView.plot(self.x1[self.i1:self.n1], self.y1[self.i1:self.n1], pen =[255,0,0], name = self.name1  )
                self.graphicsView.plot(self.x2[self.i2:self.n2], self.y2[self.i2:self.n2] , pen =[0,255,0], name=self.name2)
                self.graphicsView.plot(self.x3[self.i3:self.n3], self.y3[self.i3:self.n3], pen =[0,0,255], name=self.name3 )
                QtCore.QCoreApplication.processEvents()

    def faster(self):
        if self.comboBox_For_selecting_Channel.currentIndex()==0:
            while self.i1 < len(self.x1) and self.st == 0:
                if self.zm == 0:
                    self.graphicsView.clear()
                    self.graphicsView.plot(self.x1[self.i1:self.n1], self.y1[self.i1:self.n1], pen =[255,0,0], name=self.name1)
                    QtCore.QCoreApplication.processEvents()
                    self.n1 += 30
                    self.i1 += 10
                else:
                    self.graphicsView.clear()
                    self.graphicsView.plot(self.x1[self.i1:self.n1 // 2], self.y1[self.i1:self.n1 // 2], pen =[255,0,0], name=self.name1)
                    QtCore.QCoreApplication.processEvents()
                    self.n1 += 30
                    self.i1 += 10
        elif self.comboBox_For_selecting_Channel.currentIndex() == 1:
            while self.i2 < len(self.x2) and self.st == 0:
                if self.zm == 0:
                    self.graphicsView.clear()
                    self.graphicsView.plot(self.x2[self.i2:self.n2], self.y2[self.i2:self.n2], pen =[0,255,0], name=self.name2)
                    self.graphicsView.plot(self.x1[self.i1:self.n1], self.y1[self.i1:self.n1], pen =[255,0,0], name=self.name1)
                    QtCore.QCoreApplication.processEvents()
                    self.n1 += 30
                    self.i1 += 10
                    self.n2 += 30
                    self.i2 += 10
                else:
                    self.graphicsView.clear()
                    self.graphicsView.plot(self.x2[self.i2:self.n2 // 2], self.y2[self.i2:self.n2 // 2], pen =[0,255,0], name=self.name2)
                    self.graphicsView.plot(self.x1[self.i1:self.n1 // 2], self.y1[self.i1:self.n1 // 2], pen =[255,0,0], name=self.name1)
                    QtCore.QCoreApplication.processEvents()
                    self.n1 += 30
                    self.i1 += 10
                    self.n2 += 30
                    self.i2 += 10
        elif self.comboBox_For_selecting_Channel.currentIndex() == 2:
            while self.i3 < len(self.x3) and self.st == 0:
                if self.zm == 0:
                    self.graphicsView.clear()
                    self.graphicsView.plot(self.x3[self.i3:self.n3], self.y3[self.i3:self.n3], pen =[0,0,255], name=self.name3)
                    self.graphicsView.plot(self.x2[self.i2:self.n2], self.y2[self.i2:self.n2], pen =[0,255,0], name=self.name2)
                    self.graphicsView.plot(self.x1[self.i1:self.n1], self.y1[self.i1:self.n1], pen =[255,0,0], name=self.name1)
                    QtCore.QCoreApplication.processEvents()
                    self.n1 += 30
                    self.i1 += 10
                    self.n2 += 30
                    self.i2 += 10
                    self.n3 += 30
                    self.i3 += 10
                else:
                    self.graphicsView.clear()
                    self.graphicsView.plot(self.x3[self.i3:self.n3 // 2], self.y3[self.i3:self.n3 // 2], pen =[0,0,255], name=self.name3)
                    self.graphicsView.plot(self.x2[self.i2:self.n2 // 2], self.y2[self.i2:self.n2 // 2], pen =[0,255,0], name=self.name2)
                    self.graphicsView.plot(self.x1[self.i1:self.n1 // 2], self.y1[self.i1:self.n1 // 2], pen =[255,0,0], name=self.name1)
                    QtCore.QCoreApplication.processEvents()
                    self.n1 += 30
                    self.i1 += 10
                    self.n2 += 30
                    self.i2 += 10
                    self.n3 += 30
                    self.i3 += 10
    def slower(self):
        if self.comboBox_For_selecting_Channel.currentIndex()==0:
            while self.i1 < len(self.x1) and self.st == 0:
                if self.zm == 0:
                    self.graphicsView.clear()
                    self.graphicsView.plot(self.x1[self.i1:self.n1], self.y1[self.i1:self.n1], pen =[255,0,0], name=self.name1)
                    QtCore.QCoreApplication.processEvents()
                    self.n1 += 15
                    self.i1 += 5
                else:
                    self.graphicsView.clear()
                    self.graphicsView.plot(self.x1[self.i1:self.n1 // 2], self.y1[self.i1:self.n1 // 2], pen =[255,0,0], name=self.name1)
                    QtCore.QCoreApplication.processEvents()
                    self.n1 += 15
                    self.i1 += 5
        elif self.comboBox_For_selecting_Channel.currentIndex() == 1:
            while self.i2 < len(self.x2) and self.st == 0:
                if self.zm == 0:
                    self.graphicsView.clear()
                    self.graphicsView.plot(self.x2[self.i2:self.n2], self.y2[self.i2:self.n2], pen =[0,255,0], name=self.name2)
                    self.graphicsView.plot(self.x1[self.i1:self.n1], self.y1[self.i1:self.n1], pen =[255,0,0], name=self.name1)
                    QtCore.QCoreApplication.processEvents()
                    self.n1 += 15
                    self.i1 += 5
                    self.n2 += 15
                    self.i2 += 5
                else:
                    self.graphicsView.clear()
                    self.graphicsView.plot(self.x2[self.i2:self.n2 // 2], self.y2[self.i2:self.n2 // 2], pen =[0,255,0], name=self.name2)
                    self.graphicsView.plot(self.x1[self.i1:self.n1 // 2], self.y1[self.i1:self.n1 // 2], pen =[255,0,0], name=self.name1)
                    QtCore.QCoreApplication.processEvents()
                    self.n1 += 15
                    self.i1 += 5
                    self.n2 += 15
                    self.i2 += 5
        elif self.comboBox_For_selecting_Channel.currentIndex() == 2:
            while self.i3 < len(self.x3) and self.st == 0:
                if self.zm == 0:
                    self.graphicsView.clear()
                    self.graphicsView.plot(self.x3[self.i3:self.n3], self.y3[self.i3:self.n3], pen =[0,0,255], name=self.name3)
                    self.graphicsView.plot(self.x2[self.i2:self.n2], self.y2[self.i2:self.n2], pen =[0,255,0], name=self.name2)
                    self.graphicsView.plot(self.x1[self.i1:self.n1], self.y1[self.i1:self.n1], pen =[255,0,0], name=self.name1)
                    QtCore.QCoreApplication.processEvents()
                    self.n1 += 15
                    self.i1 += 5
                    self.n2 += 15
                    self.i2 += 5
                    self.n3 += 15
                    self.i3 += 5
                else:
                    self.graphicsView.clear()
                    self.graphicsView.plot(self.x3[self.i3:self.n3 // 2], self.y3[self.i3:self.n3 // 2], pen =[0,0,255], name=self.name3)
                    self.graphicsView.plot(self.x2[self.i2:self.n2 // 2], self.y2[self.i2:self.n2 // 2], pen =[0,255,0], name=self.name2)
                    self.graphicsView.plot(self.x1[self.i1:self.n1 // 2], self.y1[self.i1:self.n1 // 2], pen =[255,0,0], name=self.name1)
                    QtCore.QCoreApplication.processEvents()
                    self.n1 += 15
                    self.i1 += 5
                    self.n2 += 15
                    self.i2 += 5
                    self.n3 += 15
                    self.i3 += 5

    def getFile(self):
        self.st = 0
        self.filename = QFileDialog.getOpenFileName(filter="txt (*.txt)")[0]
        if self.comboBox_For_selecting_Channel.currentIndex()==0:
            self.i1 = 0
            self.n1 = 100
            self.name1= os.path.basename(self.filename)
        elif self.comboBox_For_selecting_Channel.currentIndex()==1:
            self.i1 = 0
            self.n1 = 100
            self.i2 = 0
            self.n2 = 100
            self.name2= os.path.basename(self.filename)
        elif self.comboBox_For_selecting_Channel.currentIndex() ==2:
            self.i1 = 0
            self.n1 = 100
            self.i2 = 0
            self.n2 = 100
            self.i3 = 0
            self.n3 = 100
            self.name3= os.path.basename(self.filename)
        self.readdatatxt()

    def readdatatxt(self):
        plots = np.genfromtxt(self.filename, delimiter='\t') 
        self.graphicsView.plotItem.setTitle("Channel ")
        self.graphicsView.plotItem.addLegend(frame=True)
        self.graphicsView.plotItem.showGrid(True, True, alpha=1)
        if self.comboBox_For_selecting_Channel.currentIndex()==0:
            self.x1 = plots[:, 0]
            self.y1 = plots[:, 1]
            self.spec()
            while self.i1 < len(self.x1) and self.st == 0 :
                if self.zm == 0:
                    self.graphicsView.clear()
                    self.graphicsView.plot(self.x1[self.i1:self.n1], self.y1[self.i1:self.n1], pen =[255,0,0], name = self.name1 )
                    QtCore.QCoreApplication.processEvents()
                    self.n1 += 10
                    self.i1 += 5
                else:
                    self.graphicsView.clear()
                    self.graphicsView.plot(self.x1[self.i1:self.n1 // 2], self.y1[self.i1:self.n1 // 2], pen =[255,0,0], name=self.name1)
                    QtCore.QCoreApplication.processEvents()
                    self.n1 += 3
                    self.i1 += 1
        elif self.comboBox_For_selecting_Channel.currentIndex()==1:
            self.x2 = plots[:, 0]
            self.y2 = plots[:, 1]
            self.spec()
            while self.i2 < len(self.x2) and self.st == 0 :
                if self.zm == 0 :
                    self.graphicsView.clear()
                    self.graphicsView.plot(self.x2[self.i2:self.n2], self.y2[self.i2:self.n2], pen =[0,255,0], name=self.name2)
                    self.graphicsView.plot(self.x1[self.i1:self.n1], self.y1[self.i1:self.n1], pen =[255,0,0], name=self.name1)
                    QtCore.QCoreApplication.processEvents()
                    self.n1 += 10
                    self.i1 += 5
                    self.n2 += 10
                    self.i2 += 5
                else:
                    self.graphicsView.clear()
                    self.graphicsView.plot(self.x2[self.i2:self.n2 // 2], self.y2[self.i2:self.n2 // 2], pen =[0,255,0], name=self.name2)
                    self.graphicsView.plot(self.x1[self.i1:self.n1 // 2], self.y1[self.i1:self.n1 // 2], pen =[255,0,0], name=self.name1)
                    QtCore.QCoreApplication.processEvents()
                    self.n1 += 3
                    self.i1 += 1
                    self.n2 += 3
                    self.i2 += 1
        elif self.comboBox_For_selecting_Channel.currentIndex() ==2:
            self.x3 = plots[:, 0]
            self.y3 = plots[:, 1]
            self.graphicsView.plotItem.addLegend(size=(5, 7))
            self.spec()
            while self.i3 < len(self.x3) and self.st == 0:
                if self.zm == 0:
                    self.graphicsView.clear()
                    self.graphicsView.plot(self.x3[self.i3:self.n3], self.y3[self.i3:self.n3], pen =[0,0,255], name=self.name3)
                    self.graphicsView.plot(self.x2[self.i2:self.n2], self.y2[self.i2:self.n2], pen =[0,255,0], name=self.name2)
                    self.graphicsView.plot(self.x1[self.i1:self.n1], self.y1[self.i1:self.n1], pen =[255,0,0], name=self.name1)
                    QtCore.QCoreApplication.processEvents()
                    self.n1 += 10
                    self.i1 += 5
                    self.n2 += 10
                    self.i2 += 5
                    self.n3 += 10
                    self.i3 += 5
                else:
                    self.graphicsView.clear()
                    self.graphicsView.plot(self.x2[self.i2:self.n2 // 2], self.y2[self.i2:self.n2 // 2], pen =[0,255,0], name=self.name2)
                    self.graphicsView.plot(self.x1[self.i1:self.n1 // 2], self.y1[self.i1:self.n1 // 2], pen =[255,0,0], name=self.name1)
                    self.graphicsView.plot(self.x3[self.i3:self.n3 // 2], self.y3[self.i3:self.n3 // 2], pen =[0,0,255], name=self.name3)
                    QtCore.QCoreApplication.processEvents()
                    self.n1 += 3
                    self.i1 += 1
                    self.n2 += 3
                    self.i2 += 1
                    self.n3 += 3
                    self.i3 += 1

    def spec(self):
        self.verticalLayout_6.addWidget(self.canvas)
        self.canvas.axes.cla()
        if self.comboBox_For_selecting_Channel.currentIndex()==0:
            self.plt.specgram(self.y1, Fs=10)
        elif self.comboBox_For_selecting_Channel.currentIndex()==1:
            self.plt.specgram(self.y2, Fs=10)
        elif self.comboBox_For_selecting_Channel.currentIndex()==2:
            self.plt.specgram(self.y3, Fs=10)
    def IsChecked(self):
        if (self.Channel_1_Check_Box.isChecked()==True) and (self.Channel_2_Check_Box.isChecked()==True) and (self.Channel_3_Check_Box.isChecked()==True):
            while self.i3 < len(self.x3) and self.st == 0:
                if self.zm == 0:
                    self.graphicsView.clear()
                    self.graphicsView.plot(self.x3[self.i3:self.n3], self.y3[self.i3:self.n3], pen =[0,0,255], name=self.name3)
                    self.graphicsView.plot(self.x2[self.i2:self.n2], self.y2[self.i2:self.n2], pen =[0,255,0], name=self.name2)
                    self.graphicsView.plot(self.x1[self.i1:self.n1], self.y1[self.i1:self.n1], pen =[255,0,0], name=self.name1)
                    QtCore.QCoreApplication.processEvents()
                    self.n1 += 10
                    self.i1 += 5
                    self.n2 += 10
                    self.i2 += 5
                    self.n3 += 10
                    self.i3 += 5
                else:
                    self.graphicsView.clear()
                    self.graphicsView.plot(self.x2[self.i2:self.n2 // 2], self.y2[self.i2:self.n2 // 2], pen =[0,255,0], name=self.name1)
                    self.graphicsView.plot(self.x1[self.i1:self.n1 // 2], self.y1[self.i1:self.n1 // 2], pen =[255,0,0], name=self.name1)
                    self.graphicsView.plot(self.x3[self.i3:self.n3 // 2], self.y3[self.i3:self.n3 // 2], pen =[0,0,255], name=self.name1)
                    QtCore.QCoreApplication.processEvents()
                    self.n1 += 3
                    self.i1 += 1
                    self.n2 += 3
                    self.i2 += 1
                    self.n3 += 3
                    self.i3 += 1
        if (self.Channel_1_Check_Box.isChecked()==False) and (self.Channel_2_Check_Box.isChecked()==False) and (self.Channel_3_Check_Box.isChecked()==False):
            while self.i3 < len(self.x3) and self.st == 0:
                if self.zm == 0:
                    self.graphicsView.clear()
                    # self.graphicsView.plot(self.x3[self.i3:self.n3], self.y3[self.i3:self.n3], pen =[0,0,255], name=self.name3)
                    # self.graphicsView.plot(self.x2[self.i2:self.n2], self.y2[self.i2:self.n2], pen =[0,255,0], name=self.name2)
                    # self.graphicsView.plot(self.x1[self.i1:self.n1], self.y1[self.i1:self.n1], pen =[255,0,0], name=self.name1)
                    QtCore.QCoreApplication.processEvents()
                    self.n1 += 10
                    self.i1 += 5
                    self.n2 += 10
                    self.i2 += 5
                    self.n3 += 10
                    self.i3 += 5
                else:
                    self.graphicsView.clear()
                    # self.graphicsView.plot(self.x2[self.i2:self.n2 // 2], self.y2[self.i2:self.n2 // 2], pen =[0,255,0], name=self.name1)
                    # self.graphicsView.plot(self.x1[self.i1:self.n1 // 2], self.y1[self.i1:self.n1 // 2], pen =[255,0,0], name=self.name1)
                    # self.graphicsView.plot(self.x3[self.i3:self.n3 // 2], self.y3[self.i3:self.n3 // 2], pen =[0,0,255], name=self.name1)
                    QtCore.QCoreApplication.processEvents()
                    self.n1 += 3
                    self.i1 += 1
                    self.n2 += 3
                    self.i2 += 1
                    self.n3 += 3
                    self.i3 += 1
        if (self.Channel_1_Check_Box.isChecked()==False) and (self.Channel_2_Check_Box.isChecked()==True) and (self.Channel_3_Check_Box.isChecked()==True):
            while self.i3 < len(self.x3) and self.st == 0:
                if self.zm == 0:
                    self.graphicsView.clear()
                    self.graphicsView.plot(self.x3[self.i3:self.n3], self.y3[self.i3:self.n3], pen =[0,0,255], name=self.name3)
                    self.graphicsView.plot(self.x2[self.i2:self.n2], self.y2[self.i2:self.n2], pen =[0,255,0], name=self.name2)
                    #self.graphicsView.plot(self.x1[self.i1:self.n1], self.y1[self.i1:self.n1], pen =[255,0,0], name=self.name1)
                    QtCore.QCoreApplication.processEvents()
                    self.n1 += 10
                    self.i1 += 5
                    self.n2 += 10
                    self.i2 += 5
                    self.n3 += 10
                    self.i3 += 5
                else:
                    self.graphicsView.clear()
                    self.graphicsView.plot(self.x2[self.i2:self.n2 // 2], self.y2[self.i2:self.n2 // 2], pen =[0,255,0], name=self.name2)
                    #self.graphicsView.plot(self.x1[self.i1:self.n1 // 2], self.y1[self.i1:self.n1 // 2], pen =[255,0,0], name=self.name1)
                    self.graphicsView.plot(self.x3[self.i3:self.n3 // 2], self.y3[self.i3:self.n3 // 2], pen =[0,0,255], name=self.name3)
                    QtCore.QCoreApplication.processEvents()
                    self.n1 += 3
                    self.i1 += 1
                    self.n2 += 3
                    self.i2 += 1
                    self.n3 += 3
                    self.i3 += 1
        if (self.Channel_1_Check_Box.isChecked()==True) and (self.Channel_2_Check_Box.isChecked()==False) and (self.Channel_3_Check_Box.isChecked()==True):
            while self.i3 < len(self.x3) and self.st == 0:
                if self.zm == 0:
                    self.graphicsView.clear()
                    self.graphicsView.plot(self.x3[self.i3:self.n3], self.y3[self.i3:self.n3], pen =[0,0,255], name=self.name3)
                    #self.graphicsView.plot(self.x2[self.i2:self.n2], self.y2[self.i2:self.n2], pen =[0,255,0], name=self.name2)
                    self.graphicsView.plot(self.x1[self.i1:self.n1], self.y1[self.i1:self.n1], pen =[255,0,0], name=self.name1)
                    QtCore.QCoreApplication.processEvents()
                    self.n1 += 10
                    self.i1 += 5
                    self.n2 += 10
                    self.i2 += 5
                    self.n3 += 10
                    self.i3 += 5
                else:
                    self.graphicsView.clear()
                    #self.graphicsView.plot(self.x2[self.i2:self.n2 // 2], self.y2[self.i2:self.n2 // 2], pen =[0,255,0], name=self.name2)
                    self.graphicsView.plot(self.x1[self.i1:self.n1 // 2], self.y1[self.i1:self.n1 // 2], pen =[255,0,0], name=self.name1)
                    self.graphicsView.plot(self.x3[self.i3:self.n3 // 2], self.y3[self.i3:self.n3 // 2], pen =[0,0,255], name=self.name3)
                    QtCore.QCoreApplication.processEvents()
                    self.n1 += 3
                    self.i1 += 1
                    self.n2 += 3
                    self.i2 += 1
                    self.n3 += 3
                    self.i3 += 1
        if (self.Channel_1_Check_Box.isChecked()==True) and (self.Channel_2_Check_Box.isChecked()==True) and (self.Channel_3_Check_Box.isChecked()==False):
            while self.i3 < len(self.x3) and self.st == 0:
                if self.zm == 0:
                    self.graphicsView.clear()
                    #self.graphicsView.plot(self.x3[self.i3:self.n3], self.y3[self.i3:self.n3], pen =[0,0,255], name=self.name3)
                    self.graphicsView.plot(self.x2[self.i2:self.n2], self.y2[self.i2:self.n2], pen =[0,255,0], name=self.name2)
                    self.graphicsView.plot(self.x1[self.i1:self.n1], self.y1[self.i1:self.n1], pen =[255,0,0], name=self.name1)
                    QtCore.QCoreApplication.processEvents()
                    self.n1 += 10
                    self.i1 += 5
                    self.n2 += 10
                    self.i2 += 5
                    self.n3 += 10
                    self.i3 += 5
                else:
                    self.graphicsView.clear()
                    self.graphicsView.plot(self.x2[self.i2:self.n2 // 2], self.y2[self.i2:self.n2 // 2], pen =[0,255,0], name=self.name2)
                    self.graphicsView.plot(self.x1[self.i1:self.n1 // 2], self.y1[self.i1:self.n1 // 2], pen =[255,0,0], name=self.name1)
                    #self.graphicsView.plot(self.x3[self.i3:self.n3 // 2], self.y3[self.i3:self.n3 // 2], pen =[0,0,255], name=self.name3)
                    QtCore.QCoreApplication.processEvents()
                    self.n1 += 3
                    self.i1 += 1
                    self.n2 += 3
                    self.i2 += 1
                    self.n3 += 3
                    self.i3 += 1
        if (self.Channel_1_Check_Box.isChecked()==False) and (self.Channel_2_Check_Box.isChecked()==False) and (self.Channel_3_Check_Box.isChecked()==True):
            while self.i3 < len(self.x3) and self.st == 0:
                if self.zm == 0:
                    self.graphicsView.clear()
                    self.graphicsView.plot(self.x3[self.i3:self.n3], self.y3[self.i3:self.n3], pen =[0,0,255], name=self.name3)
                    #self.graphicsView.plot(self.x2[self.i2:self.n2], self.y2[self.i2:self.n2], pen =[0,255,0], name=self.name2)
                    #self.graphicsView.plot(self.x1[self.i1:self.n1], self.y1[self.i1:self.n1], pen =[255,0,0], name=self.name1)
                    QtCore.QCoreApplication.processEvents()
                    self.n1 += 10
                    self.i1 += 5
                    self.n2 += 10
                    self.i2 += 5
                    self.n3 += 10
                    self.i3 += 5
                else:
                    self.graphicsView.clear()
                    #self.graphicsView.plot(self.x2[self.i2:self.n2 // 2], self.y2[self.i2:self.n2 // 2], pen =[0,255,0], name=self.name2)
                    #self.graphicsView.plot(self.x1[self.i1:self.n1 // 2], self.y1[self.i1:self.n1 // 2], pen =[255,0,0], name=self.name1)
                    self.graphicsView.plot(self.x3[self.i3:self.n3 // 2], self.y3[self.i3:self.n3 // 2], pen =[0,0,255], name=self.name3)
                    QtCore.QCoreApplication.processEvents()
                    self.n1 += 3
                    self.i1 += 1
                    self.n2 += 3
                    self.i2 += 1
                    self.n3 += 3
                    self.i3 += 1
        if (self.Channel_1_Check_Box.isChecked()==True) and (self.Channel_2_Check_Box.isChecked()==False) and (self.Channel_3_Check_Box.isChecked()==False):
            while self.i3 < len(self.x3) and self.st == 0:
                if self.zm == 0:
                    self.graphicsView.clear()
                    #self.graphicsView.plot(self.x3[self.i3:self.n3], self.y3[self.i3:self.n3], pen =[0,0,255], name=self.name3)
                    #self.graphicsView.plot(self.x2[self.i2:self.n2], self.y2[self.i2:self.n2], pen =[0,255,0], name=self.name2)
                    self.graphicsView.plot(self.x1[self.i1:self.n1], self.y1[self.i1:self.n1], pen =[255,0,0], name=self.name1)
                    QtCore.QCoreApplication.processEvents()
                    self.n1 += 10
                    self.i1 += 5
                    self.n2 += 10
                    self.i2 += 5
                    self.n3 += 10
                    self.i3 += 5
                else:
                    self.graphicsView.clear()
                    #self.graphicsView.plot(self.x2[self.i2:self.n2 // 2], self.y2[self.i2:self.n2 // 2], pen =[0,255,0], name=self.name2)
                    self.graphicsView.plot(self.x1[self.i1:self.n1 // 2], self.y1[self.i1:self.n1 // 2], pen =[255,0,0], name=self.name1)
                    #self.graphicsView.plot(self.x3[self.i3:self.n3 // 2], self.y3[self.i3:self.n3 // 2], pen =[0,0,255], name=self.name3)
                    QtCore.QCoreApplication.processEvents()
                    self.n1 += 3
                    self.i1 += 1
                    self.n2 += 3
                    self.i2 += 1
                    self.n3 += 3
                    self.i3 += 1
        if (self.Channel_1_Check_Box.isChecked()==False) and (self.Channel_2_Check_Box.isChecked()==True) and (self.Channel_3_Check_Box.isChecked()==False):
            while self.i3 < len(self.x3) and self.st == 0:
                if self.zm == 0:
                    self.graphicsView.clear()
                    #self.graphicsView.plot(self.x3[self.i3:self.n3], self.y3[self.i3:self.n3], pen =[0,0,255], name=self.name3)
                    self.graphicsView.plot(self.x2[self.i2:self.n2], self.y2[self.i2:self.n2], pen =[0,255,0], name=self.name2)
                    #self.graphicsView.plot(self.x1[self.i1:self.n1], self.y1[self.i1:self.n1], pen =[255,0,0], name=self.name1)
                    QtCore.QCoreApplication.processEvents()
                    self.n1 += 10
                    self.i1 += 5
                    self.n2 += 10
                    self.i2 += 5
                    self.n3 += 10
                    self.i3 += 5
                else:
                    self.graphicsView.clear()
                    self.graphicsView.plot(self.x2[self.i2:self.n2 // 2], self.y2[self.i2:self.n2 // 2], pen =[0,255,0], name=self.name2)
                    #self.graphicsView.plot(self.x1[self.i1:self.n1 // 2], self.y1[self.i1:self.n1 // 2], pen =[255,0,0], name=self.name1)
                    #self.graphicsView.plot(self.x3[self.i3:self.n3 // 2], self.y3[self.i3:self.n3 // 2], pen =[0,0,255], name=self.name3)
                    QtCore.QCoreApplication.processEvents()
                    self.n1 += 3
                    self.i1 += 1
                    self.n2 += 3
                    self.i2 += 1
                    self.n3 += 3
                    self.i3 += 1
        
    def ExportPDF(self):
        from matplotlib import pyplot as plt
        import statistics
        from fractions import Fraction as fr
        fig = plt.figure()
        plots = np.genfromtxt(self.filename, delimiter='\t')
        self.x_axis = plots[:, 0]
        self.y_axis = plots[0, :]
        max_valx_f = "{:.4f}".format(max(self.x_axis))
        min_valx_f = "{:.4f}".format(min(self.x_axis))
        max_valy_f = "{:.4f}".format(max(self.y_axis))
        min_valy_f = "{:.4f}".format(min(self.y_axis))
        Sumx = sum(self.x_axis)
        Sumy = sum(self.y_axis)
        lenx = len(self.x_axis)
        leny = len(self.y_axis)
        AvgX_f = "{:.4f}".format(Sumx/lenx)
        AvgY_f = "{:,.4f}".format(Sumy/leny)
        mode_valy_f = "{:.4f}".format(statistics.mode(self.y_axis))
        variance_valy_f = "{:.4f}".format(statistics.variance(self.y_axis))
        std_f = "{:.4f}".format(statistics.stdev(self.y_axis))
        if self.comboBox_For_selecting_Channel.currentIndex() == 0:
            fig = plt.figure()
            axis1 = fig.add_subplot(211)
            axis1.plot(self.x1,self.y1)
            axis2 = fig.add_subplot(212)
            axis2.specgram(self.y1, Fs=10)
            txt1 = ["Max X = %s" % max_valx_f,"Max Freq = %s" % max_valy_f]
            txt2 = ["Min X = %s" % min_valx_f,"Min Freq = %s" % min_valy_f]
            txt3 = ["Avg X = %s" %  AvgX_f,"Avg Freq = %s" %  AvgY_f]
            txt4 = ["ModeFreq = %s" % mode_valy_f, "Var = %s" % variance_valy_f,"std = %s"%std_f]
            plt.text(0.30, 0.980, txt1, transform = fig.transFigure,size = 8)
            plt.text(0.30, 0.955, txt2, transform = fig.transFigure,size = 8)
            plt.text(0.30, 0.930, txt3, transform = fig.transFigure,size = 8)
            plt.text(0.30, 0.905, txt4, transform = fig.transFigure,size = 8)
            fig.savefig('Signal1.pdf')

        elif self.comboBox_For_selecting_Channel.currentIndex() == 1:
            fig = plt.figure()
            axis1 = fig.add_subplot(211)
            axis1.plot(self.x2, self.y2)
            axis2 = fig.add_subplot(212)
            axis2.specgram(self.y2, Fs=10)
            txt1 = ["Max X = %s" % max_valx_f,"Max Freq = %s" % max_valy_f]
            txt2 = ["Min X = %s" % min_valx_f,"Min Freq = %s" % min_valy_f]
            txt3 = ["Avg X = %s" %  AvgX_f,"Avg Freq = %s" %  AvgY_f]
            txt4 = ["ModeFreq = %s" % mode_valy_f, "Var = %s" % variance_valy_f,"std = %s"%std_f]
            plt.text(0.30, 0.980, txt1, transform = fig.transFigure,size = 8)
            plt.text(0.30, 0.955, txt2, transform = fig.transFigure,size = 8)
            plt.text(0.30, 0.930, txt3, transform = fig.transFigure,size = 8)
            plt.text(0.30, 0.905, txt4, transform = fig.transFigure,size = 8)
            fig.savefig('Signal2.pdf')

        elif self.comboBox_For_selecting_Channel.currentIndex() == 2:
            fig = plt.figure()
            axis1 = fig.add_subplot(211)
            axis1.plot(self.x3, self.y3)
            axis2 = fig.add_subplot(212)
            axis2.specgram(self.y3, Fs=10)
            txt1 = ["Max X = %s" % max_valx_f,"Max Freq = %s" % max_valy_f]
            txt2 = ["Min X = %s" % min_valx_f,"Min Freq = %s" % min_valy_f]
            txt3 = ["Avg X = %s" %  AvgX_f,"Avg Freq = %s" %  AvgY_f]
            txt4 = ["ModeFreq = %s" % mode_valy_f, "Var = %s" % variance_valy_f,"std = %s"%std_f]
            plt.text(0.30, 0.980, txt1, transform = fig.transFigure,size = 8)
            plt.text(0.30, 0.955, txt2, transform = fig.transFigure,size = 8)
            plt.text(0.30, 0.930, txt3, transform = fig.transFigure,size = 8)
            plt.text(0.30, 0.905, txt4, transform = fig.transFigure,size = 8)
            fig.savefig('Signal3.pdf')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.zoomI.setText(_translate("MainWindow", "Zoom In"))
        self.scrollF.setText(_translate("MainWindow", "Scroll Forward"))
        self.comboBox_For_selcting_color.setItemText(0, _translate("MainWindow", "Select color"))
        self.comboBox_For_selcting_color.setItemText(1, _translate("MainWindow", "Cyan"))
        self.comboBox_For_selcting_color.setItemText(2, _translate("MainWindow", "Yellow"))
        self.comboBox_For_selcting_color.setItemText(3, _translate("MainWindow", "Pink"))
        self.scrollB.setText(_translate("MainWindow", "Scroll Backward"))
        self.savePDF.setText(_translate("MainWindow", "Save to PDF"))
        self.label_For_signal_viewr.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">Signal Viewer</span></p></body></html>"))
        self.open.setText(_translate("MainWindow", "Open"))
        self.stop.setText(_translate("MainWindow", "Stop"))
        self.play.setText(_translate("MainWindow", "Play"))
        self.zoomO.setText(_translate("MainWindow", "Zoom Out"))
        self.PushButton_Speed_down.setText(_translate("MainWindow", "Speed Down"))
        self.PushButton_Speed_up.setText(_translate("MainWindow", "speed up"))
        self.label_for_control_speed.setText(_translate("MainWindow", "Control Speed"))
        self.label_for_spectroGram.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">Spectogram</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("MainWindow", "color paletes"))
        self.comboBox.setItemText(1, _translate("MainWindow", "1st"))
        self.comboBox.setItemText(2, _translate("MainWindow", "2nd"))
        self.comboBox.setItemText(3, _translate("MainWindow", "3rd"))
        self.comboBox.setItemText(4, _translate("MainWindow", "4th"))
        self.comboBox.setItemText(5, _translate("MainWindow", "5th"))
        self.Spare_button.setText(_translate("MainWindow", "select Spectro Gram"))
        self.pushButton.setText(_translate("MainWindow", "Spare"))
        self.Channel_1_Check_Box.setText(_translate("MainWindow", "Channel 1"))
        self.Channel_2_Check_Box.setText(_translate("MainWindow", "Channel 2"))
        self.Channel_3_Check_Box.setText(_translate("MainWindow", "Channel 3"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.comboBox_For_selecting_Channel.setItemText(0, _translate("MainWindow", "Channel 1"))
        self.comboBox_For_selecting_Channel.setItemText(1, _translate("MainWindow", "Channel 2"))
        self.comboBox_For_selecting_Channel.setItemText(2, _translate("MainWindow", "Channel 3"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSave_as_pdf.setText(_translate("MainWindow", "Save as .pdf"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
