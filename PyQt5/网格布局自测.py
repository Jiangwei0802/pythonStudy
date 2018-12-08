#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication,QLabel,QWidget,QLineEdit,QPushButton,QVBoxLayout,QGridLayout,QHBoxLayout


class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.user_lable = QLabel('用户名：', self)
        self.user_eidt_lin = QLineEdit(self)
        self.pwd_lable = QLabel("登陆密码：", self)
        self.pwd_edit_line = QLineEdit(self)
        self.login_btn = QPushButton('登陆', self)
        self.sigin_bt = QPushButton("注册", self)

        self.grid_layout = QGridLayout()
        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.grid_layout.addWidget(self.user_lable, 0, 0)
        self.grid_layout.addWidget(self.user_eidt_lin, 0, 1)
        self.grid_layout.addWidget(self.pwd_lable, 1, 0)
        self.grid_layout.addWidget(self.pwd_edit_line, 1, 1)

        self.grid_layout.addWidget(self.login_btn, 2, 0)
        self.grid_layout.addWidget(self.sigin_bt, 2, 1)
        # 纯grid是实现
        self.setLayout(self.grid_layout)

        # grid + v_layout实现
        # self.h_layout.addWidget(self.sigin_bt)
        # self.h_layout.addWidget(self.login_btn)
        # self.v_layout.addLayout(self.grid_layout)
        # self.v_layout.addLayout(self.h_layout)
        # self.setLayout(self.v_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
