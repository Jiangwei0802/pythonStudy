#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class Demo(QWidget):
    my_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.lable = QLabel('hello world', self)
        self.my_signal.connect(self.changeText)

    def changeText(self):
        if self.lable.text() == 'hello world':
            self.lable.setText("hello ptqt5")
        else:
            self.lable.setText("hello world")

    def mousePressEvent(self, QMouseEvent):
        self.my_signal.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
