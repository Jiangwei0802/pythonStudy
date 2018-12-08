#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, \
    QHBoxLayout, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.user_label = QLabel('Username:', self)
        self.pwd_label = QLabel('Password:', self)
        self.user_line = QLineEdit(self)
        self.pwd_line = QLineEdit(self)
        self.login_button = QPushButton('Log in', self)
        self.signin_button = QPushButton('Sign in', self)
        self.label_v_layout = QVBoxLayout()                      # 1 实例化一个垂直布局管理器QVBoxLayout
        self.line_v_layout = QVBoxLayout()                       # 2 实例化一个垂直布局管理器QVBoxLayout；
        self.button_h_layout = QHBoxLayout()                     # 3 实例化一个水平布局管理器QHBoxLayout；
        self.label_line_h_layout = QHBoxLayout()                 # 4
        self.all_v_layout = QVBoxLayout()                        # 5 这两个布局管理器用来管理1-3中的布局
        self.label_v_layout.addWidget(self.user_label)           # 6
        self.label_v_layout.addWidget(self.pwd_label)
        self.line_v_layout.addWidget(self.user_line)
        self.line_v_layout.addWidget(self.pwd_line)
        self.button_h_layout.addWidget(self.login_button)
        self.button_h_layout.addWidget(self.signin_button)
        self.label_line_h_layout.addLayout(self.label_v_layout)  # 7
        self.label_line_h_layout.addLayout(self.line_v_layout)
        self.all_v_layout.addLayout(self.label_line_h_layout)
        self.all_v_layout.addLayout(self.button_h_layout)
        self.setLayout(self.all_v_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())