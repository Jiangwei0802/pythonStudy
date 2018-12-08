import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QTextEdit
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        exitAction = QAction(QIcon('timg.jpg'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar().showMessage("Ready")

        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        # 创建一个菜单栏
        menubar = self.menuBar()
        # 添加菜单
        fileMenu = menubar.addMenu('&File')
        # 添加事件
        fileMenu.addAction(exitAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menubar')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

