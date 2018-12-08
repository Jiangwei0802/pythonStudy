#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget,QLabel, QTextEdit, QTextBrowser, QHBoxLayout, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        self.textEditLable = QLabel("QTextEdit", self)
        self.textBrowserLable = QLabel("QTextBrowser", self)
        self.textEdit = QTextEdit(self)
        self.textBrowser = QTextBrowser(self)

        self.h1_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()
        self.h2_layout = QHBoxLayout()

        self.layout_init()

    def layout_init(self):
        self.h1_layout.addWidget(self.textEditLable)
        self.h1_layout.addWidget(self.textBrowserLable)

        self.h2_layout.addWidget(self.textEdit)
        self.h2_layout.addWidget(self.textBrowser)

        self.v_layout.addLayout(self.h1_layout)
        self.v_layout.addLayout(self.h2_layout)

        self.setLayout(self.v_layout)
        self.text_change_init()
        # self.show_text_change_func

    def text_change_init(self):
        self.textEdit.textChanged.connect(self.show_text_change_func)

    def show_text_change_func(self):
        self.textBrowser.setText(self.textEdit.toPlainText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
