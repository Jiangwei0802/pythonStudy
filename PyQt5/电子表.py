#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLCDNumber, QGridLayout, QLabel, QColorDialog
from PyQt5.QtCore import Qt
from PyQt5.Qt import  QPoint, QTimer, QTime ,QRect


class Example(QLCDNumber):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("电子表")
        self.__init_data()
        self.__init_view()

    def __init_view(self):
        self.resize(200, 60)
        self.setDigitCount(8)
        self.show_time()

    def __init_data(self):
        # 初始化数据
        self.__ShowColon = True
        self.__timer = QTimer(self)
        self.__timer.timeout.connect(self.show_time)
        self.__timer.start(1000)

    def show_time(self):
        # 更新时间
        time_now = QTime.currentTime()
        time_text = time_now.toString(Qt.DefaultLocaleLongDate)

        # 冒号闪烁
        if self.__ShowColon:
            self.__ShowColon = False
        else:
            time_text = time_text.replace(':', ' ')
            self.__ShowColon = True

        self.display(time_text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())




