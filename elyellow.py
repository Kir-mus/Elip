from PySide import QtCore, QtGui
from PySide.QtGui import QPolygon, QWidget, QApplication, QMainWindow
from sys import argv, exit
from PySide.QtCore import Qt, QPoint
from PySide.QtGui import QPainter, QColor
from random import choice, randint


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(1500, 750)
        self.centralwidget = QWidget(MainWindow)
        self.label = QtGui.QLabel()
        self.label.setGeometry(QtCore.QRect(0, 0, 500, 500))
        self.PushButton = QtGui.QPushButton(self.centralwidget)
        self.PushButton.setGeometry(QtCore.QRect(0, 0, 10, 500))
        self.PushButton.setObjectName("QPushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setWindowTitle("Супрематизм")


class Main(Ui_MainWindow, QMainWindow):
    def drawing(self, qp):
        for _ in range(randint(5, 50)):
            if self.k == 0:
                qp.setBrush(QColor(choice(self.colors)))
                m = randint(1, 200)
                qp.drawEllipse(randint(0, 1500), randint(0, 750), m, m)
        self.k = 0

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.k = 1
        self.colors = ['Yellow']

    def mousePressEvent(self, event):
        if event == Qt.LeftButton:
            self.k = 0
        self.update()
        print(event.x(), event.y())

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawing(qp)


if __name__ == '__main__':
    app = QApplication(argv)
    ex = Main()
    ex.show()
    exit(app.exec_())