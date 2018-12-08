#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setGeometry(400, 300, 300, 200)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon("timg.jpg"))
        self.show()


# if __name__ == "__main__":
app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec())

