#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(300, 300)
        self.setWindowTitle("Demo")
        self.button = QPushButton("Start", self)
        self.button.clicked.connect(self.change_text)
        self.button.clicked.connect(self.change_windowsize)
        self.button.clicked.connect(self.change_windowTitle)

    def change_text(self):
        print('change text')
        self.button.setText('Stop')
        self.button.clicked.disconnect(self.change_text)

    def change_windowsize(self):
        print('change windowsize')
        self.resize(500, 500)
        self.button.clicked.disconnect(self.change_windowsize)

    def change_windowTitle(self):
        print('change windowTitle')
        self.setWindowTitle("DEMO")
        self.button.clicked.disconnect(self.change_windowTitle)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

