import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QApplication, QMainWindow, QLineEdit, QLabel)
from PyQt5.QtGui import QFont
from logic.FistDimension import FirstDimension


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.width = 150
        self.height = 30

        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a project for multi-scale modeling')

        btn = QPushButton('1D', self)
        btn.setToolTip('1D mode')
        btn.resize(self.width, self.height)
        btn.move(0, 0)

        OneDimensionLabel = QLabel("Set Dimension")

        self.textbox = QLineEdit(self)
        self.textbox.move(self.width, 0)
        self.textbox.resize(self.width, self.height)

        self.setWindowTitle('Cellular Automata')
        self.setGeometry(300, 300, 700, 600)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
