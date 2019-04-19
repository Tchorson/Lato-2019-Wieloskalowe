# import sys
# from PyQt5.QtWidgets import (QWidget, QToolTip,
#                              QPushButton, QApplication)
# from PyQt5.QtGui import QFont
#
#
# class Example(QWidget):
#
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#         QToolTip.setFont(QFont('SansSerif', 10))
#
#         self.setToolTip('This is a <b>QWidget</b> widget')
#
#         btn = QPushButton('Button', self)
#         btn.setToolTip('This is a <b>QPushButton</b> widget')
#         btn.resize(btn.sizeHint())
#         btn.move(50, 50)
#
#         self.setGeometry(300, 300, 300, 200)
#         self.setWindowTitle('Tooltips')
#         self.show()
#
#
# if __name__ == '__main__':
# #     app = QApplication(sys.argv)
# #     ex = Example()
# #     sys.exit(app.exec_())

from logic.SecondDimension import SecondDimension
from logic.FistDimension import FirstDimension
from models import Cell

if __name__ == '__main__':
    obj = FirstDimension()

    print("initializing object")
    obj.begin_the_game()

    # print(obj.return_array())
