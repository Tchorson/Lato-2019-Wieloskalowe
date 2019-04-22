# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys

import matplotlib
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QPushButton, QWidget
from logic.FistDimension import FirstDimension
from logic.SecondDimension import SecondDimension
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class Ui_Dialog(QWidget):

    def __init__(self):
        super().__init__()
        self.FirstDimensionObj = FirstDimension()
        self.width = 100
        self.iterations = 100
        self.rule = 90
        self.alive_cels_numbers = [51]

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(850, 450)
        Dialog.setMinimumSize(QtCore.QSize(850, 450))
        Dialog.setMaximumSize(QtCore.QSize(850, 450))
        Dialog.setSizeIncrement(QtCore.QSize(10, 10))
        Dialog.setBaseSize(QtCore.QSize(100, 100))
        Dialog.setAutoFillBackground(True)
        self.horizontalWidget = QtWidgets.QWidget(Dialog)
        self.horizontalWidget.setGeometry(QtCore.QRect(0, -1, 850, 441))
        self.horizontalWidget.setMinimumSize(QtCore.QSize(850, 350))
        self.horizontalWidget.setMaximumSize(QtCore.QSize(850, 450))
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.mode_menu = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.mode_menu.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.mode_menu.setContentsMargins(0, 0, 0, 0)
        self.mode_menu.setObjectName("mode_menu")
        self.tabWidget = QtWidgets.QTabWidget(self.horizontalWidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(850, 450))
        self.tabWidget.setMaximumSize(QtCore.QSize(850, 450))
        self.tabWidget.setObjectName("tabWidget")
        self.OneDimensionalTab = QtWidgets.QWidget()
        self.OneDimensionalTab.setObjectName("OneDimensionalTab")
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.OneDimensionalTab)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(0, 0, 980, 321))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.width_layout_horizontal = QtWidgets.QHBoxLayout()
        self.width_layout_horizontal.setObjectName("width_layout_horizontal")
        self.widthLabel1D = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.widthLabel1D.setMinimumSize(QtCore.QSize(60, 0))
        self.widthLabel1D.setMaximumSize(QtCore.QSize(60, 16777215))
        self.widthLabel1D.setObjectName("widthLabel1D")
        self.width_layout_horizontal.addWidget(self.widthLabel1D)
        self.widthText1D = QtWidgets.QTextEdit(self.horizontalLayoutWidget_7)
        self.widthText1D.setMinimumSize(QtCore.QSize(60, 30))
        self.widthText1D.setMaximumSize(QtCore.QSize(60, 30))
        self.widthText1D.setDocumentTitle("")
        self.widthText1D.setObjectName("widthText1D")

        self.width_layout_horizontal.addWidget(self.widthText1D)
        self.iterationsLayout = QtWidgets.QHBoxLayout()
        self.iterationsLayout.setObjectName("iterationsLayout")
        self.iterationsLabel1D = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.iterationsLabel1D.setMinimumSize(QtCore.QSize(60, 0))
        self.iterationsLabel1D.setMaximumSize(QtCore.QSize(60, 16777215))
        self.iterationsLabel1D.setObjectName("iterationsLabel1D")
        self.iterationsLayout.addWidget(self.iterationsLabel1D)
        self.iterationsText1D = QtWidgets.QTextEdit(self.horizontalLayoutWidget_7)
        self.iterationsText1D.setMinimumSize(QtCore.QSize(60, 30))
        self.iterationsText1D.setMaximumSize(QtCore.QSize(60, 30))
        self.iterationsText1D.setObjectName("iterationsText1D")
        self.iterationsLayout.addWidget(self.iterationsText1D)
        self.aliveLayout = QtWidgets.QHBoxLayout()
        self.aliveLayout.setObjectName("aliveLayout")
        self.aliveCellsArrayLabel1D = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.aliveCellsArrayLabel1D.setMinimumSize(QtCore.QSize(100, 0))
        self.aliveCellsArrayLabel1D.setMaximumSize(QtCore.QSize(100, 16777215))
        self.aliveCellsArrayLabel1D.setObjectName("aliveCellsArrayLabel1D")
        self.aliveLayout.addWidget(self.aliveCellsArrayLabel1D)
        self.aliveCellsText1D = QtWidgets.QTextEdit(self.horizontalLayoutWidget_7)
        self.aliveCellsText1D.setMinimumSize(QtCore.QSize(60, 30))
        self.aliveCellsText1D.setMaximumSize(QtCore.QSize(60, 30))
        self.aliveCellsText1D.setObjectName("aliveCellsText1D")
        self.aliveLayout.addWidget(self.aliveCellsText1D)
        self.ruleLayout = QtWidgets.QHBoxLayout()
        self.ruleLayout.setObjectName("ruleLayout")
        self.ruleLabel1D = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.ruleLabel1D.setMinimumSize(QtCore.QSize(70, 0))
        self.ruleLabel1D.setMaximumSize(QtCore.QSize(70, 16777215))
        self.ruleLabel1D.setSizeIncrement(QtCore.QSize(100, 0))
        self.ruleLabel1D.setBaseSize(QtCore.QSize(100, 0))
        self.ruleLabel1D.setObjectName("ruleLabel1D")
        self.ruleLayout.addWidget(self.ruleLabel1D)
        self.ruleText1D = QtWidgets.QTextEdit(self.horizontalLayoutWidget_7)
        self.ruleText1D.setMinimumSize(QtCore.QSize(60, 30))
        self.ruleText1D.setMaximumSize(QtCore.QSize(60, 30))
        self.ruleText1D.setObjectName("ruleText1D")
        self.ruleLayout.addWidget(self.ruleText1D)
        self.aliveLayout.addLayout(self.ruleLayout)
        self.iterationsLayout.addLayout(self.aliveLayout)
        self.width_layout_horizontal.addLayout(self.iterationsLayout)



        self.initializeGameButton1D = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.initializeGameButton1D.setMinimumSize(QtCore.QSize(60, 0))
        self.initializeGameButton1D.setMaximumSize(QtCore.QSize(60, 16777215))
        self.initializeGameButton1D.setObjectName("initializeGameButton1D")
        self.initializeGameButton1D.clicked.connect(self.initialize_click)
        self.width_layout_horizontal.addWidget(self.initializeGameButton1D)

        self.beginGameButton1D = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.beginGameButton1D.setMinimumSize(QtCore.QSize(60, 0))
        self.beginGameButton1D.setMaximumSize(QtCore.QSize(60, 16777215))
        self.beginGameButton1D.setObjectName("beginGameButton1D")
        self.beginGameButton1D.clicked.connect(self.begin_game)
        self.width_layout_horizontal.addWidget(self.beginGameButton1D)

        self.formLayout.setLayout(1, QtWidgets.QFormLayout.LabelRole, self.width_layout_horizontal)
        self.horizontalLayout_4.addLayout(self.formLayout)
        self.qpixmapLabel1D = QtWidgets.QLabel(self.OneDimensionalTab)
        self.qpixmapLabel1D.setGeometry(QtCore.QRect(300, 160, 55, 16))
        self.qpixmapLabel1D.setObjectName("qpixmapLabel1D")

        #

        self.tabWidget.addTab(self.OneDimensionalTab, "")
        self.TwoDimensionalTab = QtWidgets.QWidget()
        self.TwoDimensionalTab.setObjectName("TwoDimensionalTab")
        self.qpixmapLabel2D = QtWidgets.QLabel(self.TwoDimensionalTab)
        self.qpixmapLabel2D.setGeometry(QtCore.QRect(260, 170, 55, 16))
        self.qpixmapLabel2D.setObjectName("qpixmapLabel2D")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.TwoDimensionalTab)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(-1, 9, 851, 411))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.width_layout_horizontal_3 = QtWidgets.QHBoxLayout()
        self.width_layout_horizontal_3.setObjectName("width_layout_horizontal_3")
        self.widthLabel_2D = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.widthLabel_2D.setMinimumSize(QtCore.QSize(50, 0))
        self.widthLabel_2D.setMaximumSize(QtCore.QSize(50, 16777215))
        self.widthLabel_2D.setObjectName("widthLabel_2D")
        self.width_layout_horizontal_3.addWidget(self.widthLabel_2D)
        self.widthText_2D = QtWidgets.QTextEdit(self.formLayoutWidget_2)
        self.widthText_2D.setMinimumSize(QtCore.QSize(60, 30))
        self.widthText_2D.setMaximumSize(QtCore.QSize(60, 30))
        self.widthText_2D.setDocumentTitle("")
        self.widthText_2D.setObjectName("widthText_2D")
        self.width_layout_horizontal_3.addWidget(self.widthText_2D)
        self.iterationsLayout_3 = QtWidgets.QHBoxLayout()
        self.iterationsLayout_3.setObjectName("iterationsLayout_3")
        self.iterationsLabel_2D = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.iterationsLabel_2D.setMinimumSize(QtCore.QSize(60, 0))
        self.iterationsLabel_2D.setMaximumSize(QtCore.QSize(60, 16777215))
        self.iterationsLabel_2D.setObjectName("iterationsLabel_2D")
        self.iterationsLayout_3.addWidget(self.iterationsLabel_2D)
        self.iterationsText_2D = QtWidgets.QTextEdit(self.formLayoutWidget_2)
        self.iterationsText_2D.setMinimumSize(QtCore.QSize(60, 30))
        self.iterationsText_2D.setMaximumSize(QtCore.QSize(60, 30))
        self.iterationsText_2D.setObjectName("iterationsText_2D")
        self.iterationsLayout_3.addWidget(self.iterationsText_2D)
        self.aliveLayout_3 = QtWidgets.QHBoxLayout()
        self.aliveLayout_3.setObjectName("aliveLayout_3")
        self.aliveCellsArrayLabel_2D = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.aliveCellsArrayLabel_2D.setMinimumSize(QtCore.QSize(80, 0))
        self.aliveCellsArrayLabel_2D.setMaximumSize(QtCore.QSize(80, 16777215))
        self.aliveCellsArrayLabel_2D.setObjectName("aliveCellsArrayLabel_2D")
        self.aliveLayout_3.addWidget(self.aliveCellsArrayLabel_2D)
        self.aliveCellsText_2D = QtWidgets.QTextEdit(self.formLayoutWidget_2)
        self.aliveCellsText_2D.setMinimumSize(QtCore.QSize(60, 30))
        self.aliveCellsText_2D.setMaximumSize(QtCore.QSize(60, 30))
        self.aliveCellsText_2D.setObjectName("aliveCellsText_2D")
        self.aliveLayout_3.addWidget(self.aliveCellsText_2D)
        self.ruleLayout_3 = QtWidgets.QHBoxLayout()
        self.ruleLayout_3.setObjectName("ruleLayout_3")
        self.ruleLabel_2D = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.ruleLabel_2D.setMinimumSize(QtCore.QSize(60, 0))
        self.ruleLabel_2D.setMaximumSize(QtCore.QSize(60, 16777215))
        self.ruleLabel_2D.setObjectName("ruleLabel_2D")
        self.ruleLayout_3.addWidget(self.ruleLabel_2D)
        self.ruleText_2D = QtWidgets.QTextEdit(self.formLayoutWidget_2)
        self.ruleText_2D.setMinimumSize(QtCore.QSize(60, 30))
        self.ruleText_2D.setMaximumSize(QtCore.QSize(60, 30))
        self.ruleText_2D.setObjectName("ruleText_2D")
        self.ruleLayout_3.addWidget(self.ruleText_2D)
        self.aliveLayout_3.addLayout(self.ruleLayout_3)
        self.iterationsLayout_3.addLayout(self.aliveLayout_3)
        self.width_layout_horizontal_3.addLayout(self.iterationsLayout_3)
        self.horizontalLayout_8.addLayout(self.width_layout_horizontal_3)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_8)
        self.initializeGameButton_2D = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.initializeGameButton_2D.setMinimumSize(QtCore.QSize(60, 0))
        self.initializeGameButton_2D.setMaximumSize(QtCore.QSize(60, 16777215))
        self.initializeGameButton_2D.setObjectName("initializeGameButton_2D")
        self.horizontalLayout_7.addWidget(self.initializeGameButton_2D)
        self.beginGameButton_2D = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.beginGameButton_2D.setMinimumSize(QtCore.QSize(60, 0))
        self.beginGameButton_2D.setMaximumSize(QtCore.QSize(60, 16777215))
        self.beginGameButton_2D.setObjectName("beginGameButton_2D")
        self.horizontalLayout_7.addWidget(self.beginGameButton_2D)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_7)
        self.tabWidget.addTab(self.TwoDimensionalTab, "")
        self.mode_menu.addWidget(self.tabWidget)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Cellular-Automata:Mateusz Tchorek"))
        self.widthLabel1D.setText(_translate("Dialog", "Width"))
        self.widthText1D.setPlaceholderText(_translate("Dialog", "100"))
        self.iterationsLabel1D.setText(_translate("Dialog", "Iterations"))
        self.iterationsText1D.setPlaceholderText(_translate("Dialog", "100"))
        self.aliveCellsArrayLabel1D.setText(_translate("Dialog", "Set cell/s alive"))
        self.aliveCellsText1D.setPlaceholderText(_translate("Dialog", "51,1"))
        self.ruleLabel1D.setText(_translate("Dialog", "Rule 1-255"))
        self.ruleText1D.setPlaceholderText(_translate("Dialog", "90"))
        self.initializeGameButton1D.setText(_translate("Dialog", "Initialize"))
        self.beginGameButton1D.setText(_translate("Dialog", "Start"))
        self.qpixmapLabel1D.setText(_translate("Dialog", "QPixMap"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.OneDimensionalTab),
                                  _translate("Dialog", "OneDimensional"))
        self.qpixmapLabel2D.setText(_translate("Dialog", "QPixMap"))
        self.widthLabel_2D.setText(_translate("Dialog", "Width"))
        self.widthText_2D.setPlaceholderText(_translate("Dialog", "100"))
        self.iterationsLabel_2D.setText(_translate("Dialog", "Iterations"))
        self.iterationsText_2D.setPlaceholderText(_translate("Dialog", "100"))
        self.aliveCellsArrayLabel_2D.setText(_translate("Dialog", "Set cell/s alive"))
        self.aliveCellsText_2D.setPlaceholderText(_translate("Dialog", "51,1"))
        self.ruleLabel_2D.setText(_translate("Dialog", "Rule 1-255"))
        self.ruleText_2D.setPlaceholderText(_translate("Dialog", "90"))
        self.initializeGameButton_2D.setText(_translate("Dialog", "Initialize"))
        self.beginGameButton_2D.setText(_translate("Dialog", "Start"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TwoDimensionalTab),
                                  _translate("Dialog", "TwoDimensional"))

    @pyqtSlot()
    def initialize_click(self):
        if str(self.widthText1D.toPlainText()) != "":
            self.width = int(self.widthText1D.toPlainText())
            self.widthText1D.clear()
        if str(self.iterationsText1D.toPlainText()) != "":
            self.iterations = int( self.iterationsText1D.toPlainText())
            self.iterationsText1D.clear()

        if str(self.aliveCellsText1D.toPlainText()) != "":
            self.alive_cels_numbers = [int(element) for element in self.aliveCellsText1D.toPlainText().split(",")]
            self.aliveCellsText1D.clear()

        if str(self.ruleText1D.toPlainText()) != "":
            self.rule =  int(self.ruleText1D.toPlainText())
            self.ruleText1D.clear()

        self.FirstDimensionObj.set_parameters(self.width, self.iterations, self.rule , self.alive_cels_numbers)
        #print('parameters set')
        #print(self.FirstDimensionObj.return_parameters())

    @pyqtSlot()
    def begin_game(self):
        #self.FirstDimensionObj.begin_the_game()
        print(' ')
        counter = self.iterations
        #print(self.current_iteration_array)

        while counter >0:
            self.current_iteration_array = self.FirstDimensionObj.single_iteration()

            for element in self.current_iteration_array:
                print(element, end='')
            print("\n")
            counter-=1


# class Canvas(FigureCanvas):
#     def __init__(self,parent = None, width = 100, height = 100, dpi = 100):
#         fig = Figure(figsize=(width,height),dpi=dpi)
#         self.axes = fig.add_subplot(111)
#         FigureCanvas.__init__(self,fig)
#         self.setParent(parent)
#
#         self.plot()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
