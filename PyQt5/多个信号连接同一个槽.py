#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.button = QPushButton('Start', self)
        self.button.pressed.connect(self.change_text)
        self.button.released.connect(self.change_text)

    def change_text(self):
        if self.button.text() == 'Start':
            self.button.setText('Stop')
        else:
            self.button.setText('Start')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec())
