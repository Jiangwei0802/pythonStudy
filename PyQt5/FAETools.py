
import sys
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QLabel, QLineEdit, QDateEdit, QComboBox, QTextEdit,\
    QGridLayout, QPushButton, QRadioButton, QTextBrowser, QHBoxLayout


class Demo(QTabWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.setWindowTitle("FAETools")
        self.resize(800, 600)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QTextEdit()
        self.tab1_init()
        self.tab2_init()
        self.addTab(self.tab1, 'log check')
        self.addTab(self.tab2, 'Contact Info')
        self.addTab(self.tab3, QIcon('info.ico'), 'More Info')
        self.currentChanged.connect(lambda: print(self.currentIndex()))    # 4

    def tab1_init(self):
        h_layout = QHBoxLayout()
        mac_label = QLabel('MAC:', self.tab1)
        mac_show_lable = QComboBox()
        mac_show_lable.adjustSize()
        h_layout.addWidget(mac_label)
        h_layout.addWidget(mac_show_lable)
        ip_label = QLabel('IP:', self.tab1)
        ip_label.resize(10, 5)
        ip_show = QLabel('', self.tab1)
        h_layout.addWidget(ip_label)
        h_layout.addWidget(ip_show)
        get_infor_tn = QPushButton('获取模块信息', self.tab1)
        con_btn = QPushButton('连接', self.tab1)
        con_result = QLabel(self.tab1)
        con_result.setPixmap(QPixmap('redled.ico'))

        log_record_lable = QLabel('log记录', self.tab1)
        enable_btn = QRadioButton('enable', self.tab1)
        disable_btn = QRadioButton('disable', self.tab1)
        log_browse = QTextBrowser()

        g_layout = QGridLayout()
        g_layout.addLayout(h_layout, 0, 0, 1, 1)
        g_layout.addWidget(mac_show_lable, 0, 1, 1, 1)
        g_layout.addWidget(ip_label, 0, 2, 1, 1)
        g_layout.addWidget(ip_show, 0, 3, 1, 1)
        g_layout.addWidget(get_infor_tn, 0, 4)
        g_layout.addWidget(con_btn, 0, 5, 1, 1)
        g_layout.addWidget(con_result, 0, 6, 1, 1)
        g_layout.addWidget(log_record_lable, 0, 7, 1, 1)
        g_layout.addWidget(enable_btn, 0, 8)
        g_layout.addWidget(enable_btn, 0, 9)
        g_layout.addWidget(disable_btn, 0, 10)
        g_layout.addWidget(log_browse, 1, 0, 1, 10)
        self.tab1.setLayout(g_layout)

    def tab2_init(self):
        tel_label = QLabel('Tel:', self.tab2)
        mobile_label = QLabel('Mobile:', self.tab2)
        add_label = QLabel('Address:', self.tab2)
        tel_line = QLineEdit(self.tab2)
        mobile_line = QLineEdit(self.tab2)
        add_line = QLineEdit(self.tab2)
        g_layout = QGridLayout()
        g_layout.addWidget(tel_label, 0, 0, 1, 1)
        g_layout.addWidget(tel_line, 0, 1, 1, 1)
        g_layout.addWidget(mobile_label, 1, 0, 1, 1)
        g_layout.addWidget(mobile_line, 1, 1, 1, 1)
        g_layout.addWidget(add_label, 2, 0, 1, 1)
        g_layout.addWidget(add_line, 2, 1, 1, 1)
        self.tab2.setLayout(g_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())