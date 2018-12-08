#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 1.单个文件打开 QFileDialog.getOpenFileName()
# 2.多个文件打开 QFileDialog.getOpenFileNames()
# 3.文件夹选取 QFileDialog.getExistingDirectory()
# 4.文件保存 QFileDialog.getSaveFileName()



import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QFileDialog, QVBoxLayout, QHBoxLayout, QFileDialog, QTextBrowser


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(600, 600)
        self.text_browser = QTextBrowser()
        self.open_btn = QPushButton("打开", self)
        self.save_btn = QPushButton("保存", self)
        self.clear_btn = QPushButton("清除", self)
        self.grid_layout = QGridLayout()
        self.h_layout1 = QHBoxLayout()
        self.ui_init()
        self.btn_init()

    def ui_init(self):
        self.grid_layout.addWidget(self.text_browser, 0, 0, 1, 3)
        self.h_layout1.addWidget(self.clear_btn)
        self.h_layout1.addWidget(self.open_btn)
        self.h_layout1.addWidget(self.save_btn)
        self.grid_layout.addLayout(self.h_layout1, 1, 1)
        self.setLayout(self.grid_layout)

    def btn_init(self):
        self.open_btn.clicked.connect(self.open)
        self.clear_btn.clicked.connect(self.clear)
        self.save_btn.clicked.connect(self.save)

    def open(self):
        fileName1, ok = QFileDialog.getOpenFileName(self, "选取文件", "./", "All Files (*);;Text Files (*.txt)")   # 设置文件扩展名过滤,注意用双分号间隔
        print(fileName1, ok)
        if ok:
            _f = open(fileName1, 'r')
            with _f:
                data = _f.read()
                self.text_browser.append(data)

    def clear(self):
        self.text_browser.clear()

    def save(self):
        filename, ok = QFileDialog.getSaveFileName(self, '保存文件', 'C:/Users/jiang/Desktop')
        print(filename)
        if ok:
            # try:
            #     StrText = self.text_browser.toPlainText()
            #     qS = str(StrText)
            #     f = open(filename, 'w')
            #     print(f.write('{}'.format(qS)))
            #     f.close()
            # except Exception as e:
            #     print(e)

            #
            try:
                StrText = self.text_browser.toPlainText()
                qS = str(StrText)
                print("qS len={0}".format(len(qS)))
                f = open(filename, 'a')
                print(f.write('\n{}'.format(qS)))
                f.close()
            except Exception as e:
                print(e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

