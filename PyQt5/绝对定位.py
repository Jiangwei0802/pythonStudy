#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        lbl1 = QLabel('Zetcode', self)
        lbl1.move(15, 10)

        lbl2 = QLabel("tutorials", self)
        lbl2.move(35, 40)

        lbl3 = QLabel('For programmers', self)
        lbl3.move(55, 70)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Absolue")
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

